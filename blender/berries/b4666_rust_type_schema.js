// rust_type_schema
//
// Copied verbatim from https://github.com/XiaoJiang-Phy/CrystalCanvas
//   file scripts/ipc-inventory.mjs, line 235
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const LEGACY_TYPE_ALIASES = {
    AppSettings: 'AppSettingsDto',
    BondAnalysisResult: 'BondAnalysisResult',
    BondInfo: 'BondInfo',
    BondLengthStat: 'BondLengthStat',
    BzInfoResponse: 'BzInfo',
    BzLabelPos: 'ScreenLabel',
    CoordinationInfo: 'CoordinationInfo',
    CrystalState: 'CrystalState',
    KPathInfoResponse: 'KPathInfo',
    KPathPointUi: 'KPathPointUi',
    KPathTextResponse: 'KPathText',
    MeasurementLabelPos: 'ScreenLabel',
    MeasurementOverlay: 'MeasurementOverlay',
    PhononModeSummary: 'PhononModeSummary',
    VolumetricInfo: 'VolumetricInfo',
    WannierInfo: 'WannierInfo',
};

const RUST_NAMED_TYPE_MAP = {
    ...LEGACY_TYPE_ALIASES,
};


function normalize_rust_type(type) {
    return type.replace(/\s+/g, ' ').trim();
}


function split_top_level_parameters(source) {
    const parameters = [];
    let start = 0;
    let angle_depth = 0;
    let parenthesis_depth = 0;
    let bracket_depth = 0;
    let brace_depth = 0;
    for (let index = 0; index < source.length; index += 1) {
        const character = source[index];
        if (character === '<') angle_depth += 1;
        else if (character === '>') angle_depth -= 1;
        else if (character === '(') parenthesis_depth += 1;
        else if (character === ')') parenthesis_depth -= 1;
        else if (character === '[') bracket_depth += 1;
        else if (character === ']') bracket_depth -= 1;
        else if (character === '{') brace_depth += 1;
        else if (character === '}') brace_depth -= 1;
        else if (character === ',' && angle_depth === 0 && parenthesis_depth === 0
            && bracket_depth === 0 && brace_depth === 0) {
            parameters.push(source.slice(start, index).trim());
            start = index + 1;
        }
    }
    const tail = source.slice(start).trim();
    if (tail) parameters.push(tail);
    return parameters;
}


function generic_parts(type) {
    const opening = type.indexOf('<');
    if (opening < 0 || !type.endsWith('>')) return null;
    return {
        name: type.slice(0, opening).split('::').at(-1),
        args: split_top_level_parameters(type.slice(opening + 1, -1)),
    };
}


function rust_type_schema(raw_type) {
    const type = normalize_rust_type(raw_type).replace(/^&(?:'[^ ]+\s+)?/, '');
    if (type === '()') return 'null';
    if (['String', 'str'].includes(type)) return 'string';
    if (type === 'bool') return 'boolean';
    if (/^(?:[iu](?:8|16|32|64|128|size)|f(?:32|64))$/.test(type)) return 'number';
    const array = type.match(/^\[([\s\S]+);\s*(\d+)\]$/);
    if (array) {
        const item = rust_type_schema(array[1]);
        return `[${Array.from({ length: Number(array[2]) }, () => item).join(',')}]`;
    }
    const generic = generic_parts(type);
    if (generic?.name === 'Option' && generic.args.length === 1) {
        return [rust_type_schema(generic.args[0]), 'null'].sort().join('|');
    }
    if (generic?.name === 'Vec' && generic.args.length === 1) {
        return `Array<${rust_type_schema(generic.args[0])}>`;
    }
    if (generic?.name === 'HashMap' && generic.args.length === 2) {
        return `Record<${rust_type_schema(generic.args[0])},${rust_type_schema(generic.args[1])}>`;
    }
    if (generic?.name === 'IpcEnumInput' && generic.args.length === 1) {
        return rust_type_schema(generic.args[0]);
    }
    if (generic && ['Result', 'IpcResult'].includes(generic.name)) {
        return rust_type_schema(generic.args[0]);
    }
    const name = type.split('::').at(-1);
    return RUST_NAMED_TYPE_MAP[name] ?? name;
}
