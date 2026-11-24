# build_proactive_agent_user_message
#
# Copied verbatim from https://github.com/kiyotakali/Miru
#   file prompt.py, line 1892
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Obscure computers, languages, unusual interfaces
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import json


def build_proactive_agent_user_message(intent: dict, delivery_preflight: dict | None = None) -> str:
    """Build the meta-user message for proactive main-agent mode."""
    p = delivery_preflight if isinstance(delivery_preflight, dict) else {}
    brief = p.get("delivery_brief") if isinstance(p.get("delivery_brief"), dict) else {}
    include = brief.get("must_include") if isinstance(brief.get("must_include"), list) else []
    avoid = brief.get("must_avoid") if isinstance(brief.get("must_avoid"), list) else []
    silent_boundaries = str(brief.get("silent_boundaries") or "").strip()
    silent_boundaries_usage = str(brief.get("silent_boundaries_usage") or "").strip()
    return "\n".join([
        "【Proactive Delivery Brief】",
        "用户此刻没有直接问你问题。AttentionEngine 已经决定我应该主动开口。",
        "请把下面的开口意图转成一条像 Miru 自然靠近用户的主动消息。",
        "",
        "【Attention speak_intent】",
        json.dumps(intent if isinstance(intent, dict) else {}, ensure_ascii=False, indent=2),
        "",
        "【Delivery plan】",
        f"- source: {'AttentionEngine direct' if p.get('direct_from_attention') else 'delivery plan'}",
        f"- reason: {p.get('reason', '')}",
        f"- goal: {brief.get('goal', '')}",
        f"- tone: {brief.get('tone', '')}",
        f"- context_summary: {brief.get('context_summary', '')}",
        f"- care_motive: {brief.get('care_motive', '')}",
        f"- emotional_source: {brief.get('emotional_source', '')}",
        f"- user_need: {brief.get('user_need', '')}",
        f"- approach: {brief.get('approach', '')}",
        f"- content_anchor: {brief.get('content_anchor', '')}",
        f"- miru_impulse: {brief.get('miru_impulse', '')}",
        f"- silent_boundaries: {silent_boundaries}",
        f"- silent_boundaries_usage: {silent_boundaries_usage}",
        f"- message_seed: {brief.get('message_seed', '')}",
        f"- message_seed_usage: {brief.get('message_seed_usage', '')}",
        f"- must_include: {json.dumps(include, ensure_ascii=False)}",
        f"- must_avoid: {json.dumps(avoid, ensure_ascii=False)}",
        "",
        "【输出要求】",
        "- 只输出最终要发给用户的一条消息。",
        "- 不要解释你为什么说这句话。",
        "- 不要提系统、日志、检测、AttentionEngine 或内部判断。",
        "- 不要把 brief 当成用户问题回答。",
        "- message_seed 是灵感，不是要照抄的原文；如果照抄会显得冷，就自然改写。",
        "- silent_boundaries 是内部边界，不要把它原样说给用户；不要用“我不吵你/不打扰你/需要我就叫我”证明体贴。",
        "- 如果 approach=co_watch，优先像一起看番/视频的人一样聊具体内容或节奏；不确定内容时再聊状态。",
        "- 如果 approach=playful_react，可以活泼一点、吐槽一点、跟着紧张或开心。",
        "- 如果 approach=life_rhythm，像参与他的生活一样表达喜欢、支持或小小的安心。",
        "- 如果 approach=deep_work，少打断，只有在节点、卡点或明显疲惫时用很轻的一句靠近。",
        "- 可以 1-3 句，短但不能冷，像真的在乎、一起生活，而不是像状态灯亮一下。",
    ])
