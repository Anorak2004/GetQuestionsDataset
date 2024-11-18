import re

from bs4 import BeautifulSoup


class QuestionProcessor:
    def __init__(self, html_content):
        """
        初始化 QuestionProcessor 类。

        :param html_content: 原始 HTML 内容
        """
        self.soup = BeautifulSoup(html_content, 'html.parser')
        self.desc_divs = self.soup.find_all('div', class_='desc')

    def preprocess(self):
        """
        预处理 HTML 内容，提取所有需要的信息。
        """
        # 检查是否提取到有效的 div
        if not self.desc_divs:
            raise ValueError("没有找到任何有效的 <div class='desc'> 标签")

    def extract_question_text(self):
        """
        提取题目描述（如题干部分）。

        :return: 题目描述文本
        """
        if len(self.desc_divs) > 0:
            return self.desc_divs[0].get_text(strip=True)
        return None

    def extract_options(self):
        """
        提取选项内容。

        :return: 选项内容列表
        """
        options = []
        if len(self.desc_divs) > 1:
            options_div = self.desc_divs[1]
            for option in options_div.find_all('p'):
                options.append(option.get_text(strip=True))
        # 过滤掉第一个选项内容（如“1.选择血液检查项目的原则是：”）
        return options[1:] if options else []

    def extract_correct_answer(self):
        """
        提取正确答案。

        :return: 正确答案文本
        """
        for div in self.desc_divs:
            if "正确答案" in div.get_text():  # 查找包含“正确答案”的div
                correct_answer = div.find('b')
                if correct_answer:
                    return correct_answer.get_text(strip=True)
        return None

    def extract_analysis(self):
        """
        提取试题解析内容。

        :return: 试题解析文本
        """
        for div in self.desc_divs:
            if "试题解析" in div.get_text():  # 查找包含“试题解析”的div
                analysis = div.find('div', class_='col-xs-11')
                if analysis:
                    return analysis.get_text(strip=True)
        return None

    def process(self):
        """
        执行所有的处理步骤并返回结果。

        :return: dict 包含题目、选项、正确答案和解析
        """
        self.preprocess()

        question_text = self.extract_question_text()
        options = self.extract_options()
        correct_answer = self.extract_correct_answer()
        analysis = self.extract_analysis()
        total_number = self.get_total_questions()

        return {
            'question_text': question_text,
            'options': options,
            'correct_answer': correct_answer,
            'analysis': analysis,
            'total_number': total_number
        }

    def get_total_questions(self):
        """
        使用正则表达式提取“共多少题”的信息。
        """
        tmp_content = ' '.join([div.get_text() for div in self.desc_divs])
        match = re.search(r'共\s*(\d+)\s*题', tmp_content)
        if match:
            total_questions = match.group(1)  # 提取数字部分
            return total_questions
        else:
            return None


# 示例用法
if __name__ == "__main__":
    # html_content 为你手动提供的 HTML 内容
    html_content = '''
        <h2 class="title">
                    第 1 题
                    <a class="badge pull-right favor" data-questionid="81227">收藏</a>
                    <a class="badge pull-right error" data-questionid="81227">纠错</a>
                                <a class="jump next badge pull-right" data-number="2">下一题</a>
                                        </h2>
                <ul class="list-unstyled list-img">
                                <li class="border morepadding">
                        <div class="desc">
                            <p>1.选择血液检查项目的原则是：</p>
                        </div>
                    </li>
                                <li class="border morepadding">
                        <div class="desc">
                            <p><p>A.以高、难、新、尖项目为宜</p><p>B.项目越多越好</p><p>C.在询问病史和体格检查之后</p><p>D.根据主诉</p><p>E.价格低廉</p></p>
                        </div>
                    </li>
                                            <li class="border morepadding">
                        <form class="nopadding desc">
                                                                                        <label class="inline"><input type="radio" name="question[81227]" rel="81227" value="A" /><span class="selector">A</span> </label>
                                                                    <label class="inline"><input type="radio" name="question[81227]" rel="81227" value="B" /><span class="selector">B</span> </label>
                                                                    <label class="inline"><input type="radio" name="question[81227]" rel="81227" value="C" /><span class="selector">C</span> </label>
                                                                    <label class="inline"><input type="radio" name="question[81227]" rel="81227" value="D" /><span class="selector">D</span> </label>
                                                                    <label class="inline"><input type="radio" name="question[81227]" rel="81227" value="E" /><span class="selector">E</span> </label>
                                                                                                        </form>
                    </li>
                                <li class="border morepadding rightanswer hide">
                        <div class="intro">
                            <div class="desc">
                                <div class="col-xs-1 nopadding">
                                    <div class="toolbar"><span class="badge">正确答案</span></div>
                                </div>
                                                        <div class="col-xs-11">
                                    <b id="rightanswer_81227">C</b>
                                </div>
                                                    </div>
                        </div>
                    </li>
                    <li class="border morepadding rightanswer hide">
                        <div class="intro">
                            <div class="desc">
                                <div class="col-xs-1 nopadding">
                                    <div class="toolbar"><span class="badge">试题解析</span></div>
                                </div>
                                <div class="col-xs-11">
                                    暂无解析						</div>
                            </div>
                        </div>
                    </li>
                    <li class="border padding">
                        <div class="intro text-right">
                            <div class="desc">
                                <form class="toolbar" target="questionpanel" action="index.php?exam-app-lesson-ajax-questions&knowsid=177">
                                    共 6 题，当前第 1 题。
                                    <span class="form-inline form-group">
                                        去第 <input type="search" size="1" class="form-control text-center" name="number" placeholder="1"> 题
                                    </span>
                                </form>
                            </div>
                        </div>
                    </li>
                </ul>
                <script type="text/javascript">
                $(function(){
                    var sumquestion = function(value,qid){
                        $('.rightanswer').removeClass('hide');
                        if(value == $("#rightanswer_"+qid).html())
                        {
                            $.zoombox.show('ajaxOK',{message:'回答正确'});
                            $("#rightanswer_"+qid).attr('class','text-success');
                        }
                        else
                        {
                            $.zoombox.show('ajax',{message:'回答错误'});
                            $("#rightanswer_"+qid).attr('class','text-danger');
                        }
                        setTimeout($.zoombox.hide,1000);
                    }
                    $("input:radio").click(function(){
                        var _this = $(this);
                        var qid = _this.attr('rel');
                        sumquestion(_this.val(),qid);
                    });
                    $(".finish").click(function(){
                        var _this = $(this);
                        var qid = _this.attr('rel');
                        var parent = _this.parents("form:first");
                        var value = '';
                        if(_this.hasClass('fill')){
                            value = parent.find("input").val();
                        }
                        else{
                            parent.find("input:checked").each(function(){
                                value += $(this).val().toUpperCase();
                            });
                        }
                        if(value == '')
                        {
                            $.zoombox.show('ajax',{message:'请先答题'});
                            return;
                        }
                        sumquestion(value,qid);
                    });
                });
    
                </script>
    '''
    processor = QuestionProcessor(html_content)
    result = processor.process()

    print("题目内容:", result['question_text'])
    print("选项内容:", result['options'])
    print("正确答案:", result['correct_answer'])
    print("试题解析:", result['analysis'])
    print("题目总数:", result['total_number'])
