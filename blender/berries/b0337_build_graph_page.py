# build_graph_page
#
# Copied verbatim from https://github.com/ItIsMixian/Orrery
#   file scripts/docsite/build_docsite.py, line 487
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def build_graph_page(legend):
    return ('<article class="page wide" id="graph-page" data-kind="graph" data-title="关系图谱">'
            '<h1 class="page-title">关系图谱</h1>'
            '<p class="lead">这里只显示核心事实链：Seed、有效 ADR 与 State。Implementation、Validation、Snapshot 和 Library 仍可从分类导航与搜索抵达，但不伪装成权威事实节点。'
            '<b style="color:#b083f0">紫线</b>=决策关系，灰线=核心文档中的实际引用。悬停高亮，点击跳转，拖拽重排。</p>'
            '<div class="gwrap"><svg id="graph"></svg><div class="legend">' + legend + '</div>'
            '<div class="ghint">拖背景平移 · 滚轮缩放 · 拖动节点 · 点击跳转</div></div></article>')
