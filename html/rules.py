# encoding: utf-8
#有了处理程序和文本块生成器，接下来就需要一定的规则来判断每个文本块交给处理程序将要加什么标记，rules.py 代码如下：
class Rule:
    """
    规则父类
    """
    def action(self, block, handler):
        """
        加标记
        """
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True

class HeadingRule(Rule):
    """
    一号标题规则
    """
    type = 'heading'
    def condition(self, block):
        """
        判断文本块是否符合规则
        """
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'

class TitleRule(HeadingRule):
    """
    二号标题规则
    """
    type = 'title'
    first = True

    def condition(self, block):
        if not self.first: return False
        self.first = False
        return HeadingRule.condition(self, block)

class ListItemRule(Rule):
    """
    列表项规则
    """
    type = 'listitem'
    def condition(self, block):
        return block[0] == '-'

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True

class ListRule(ListItemRule):
    """
    列表规则
    """
    type = 'list'
    inside = False
    def condition(self, block):
        return True

    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False

class ParagraphRule(Rule):
    """
    段落规则
    """
    type = 'paragraph'

    def condition(self, block):
        return True