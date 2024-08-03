from crewai import Task
from textwrap import dedent

class SCOATasks:
    def strength_analysis_task(self, strengths_analyst, academic_scores, study_profile, cognitive_inputs):
        return Task(
            description=dedent(f"""
                Analyse and find the student's strengths based on the academic confidence scores, study profile and cognitive questionnaire responses.
                This task involves analysing each question-response pair given to you, then comparing with the benchmark data provided and finally identifying:
                - what topics he/she is displaying strong confidence in, and hence can score very high marks.
                - if the student is strong in a certain topic and if that topic has high weightage (based on benchmark data), then consider it as his/her strength.
                - what study behaviour he/she is having that is enabling him/her to achieve good performance.
                - what cognitive feature he/she is being very helpful in his/her learning, practising and improving abilities.
                    
                Academic Confidence Scores:
                    Physics:
                    {SCOAHelpers.format_scores(academic_scores['physics'])}
                        
                    Chemistry:
                    {SCOAHelpers.format_scores(academic_scores['chemistry'])}
                        
                    Mathematics:
                    {SCOAHelpers.format_scores(academic_scores['maths'])}
                    
                Study Profile:
                {SCOAHelpers.format_qa_pairs(study_profile)}
                    
                Cognitive Inputs:
                {SCOAHelpers.format_qa_pairs(cognitive_inputs)}
                    
                Based on this information, provide a detailed report of the student's strengths.
                Consider their strong subjects, effective study habits, and cognitive abilities that contribute to their success.
                Ensure that all the strengths discussed are mostly in context of JEE preparation only.
                
                {SCOAHelpers.bonus_section()}
            """),
            agent=strengths_analyst,
            async_execution=True,
            expected_output="Your final answer should be a comprehensive report on the student's strengths, backed by the data provided."
        )
    
    def challenges_analysis_task(self, challenges_analyst, academic_scores, study_profile, cognitive_inputs):
        return Task(
            description=dedent(f"""
                Analyse and find the challenges the student is facing based on the academic confidence scores, study profile and cognitive questionnaire responses.
                This task involves analysing each question-response pair given to you, then comparing with the benchmark data provided and finally identifying characteristics like:
                - what topics he/she is displaying weak to average confidence in, and is unable to score good marks.
                - if the student is weak to average in a certain topic and if that topic has medium to high weightage (based on benchmark data), then consider it as his/her challenge that needs to be overcomed.
                - what study behaviour he/she is having that may be adding up to his/her challenge.
                - what cognitive feature he/she is having that may be adding to his/her challenges.
                    
                Academic Confidence Scores:
                    Physics:
                    {SCOAHelpers.format_scores(academic_scores['physics'])}
                        
                    Chemistry:
                    {SCOAHelpers.format_scores(academic_scores['chemistry'])}
                        
                    Mathematics:
                    {SCOAHelpers.format_scores(academic_scores['maths'])}
                    
                Study Profile:
                {SCOAHelpers.format_qa_pairs(study_profile)}
                    
                Cognitive Inputs:
                {SCOAHelpers.format_qa_pairs(cognitive_inputs)}
                    
                Based on this information, provide a detailed report of the student's potential challenges.
                Consider their weak subjects, ineffective study habits, and inadequate cognitive abilities that contribute to their challenges.
                Ensure that all the challenges discussed are strictly in context of JEE preparation only.
                
                {SCOAHelpers.bonus_section()}
            """),
            agent=challenges_analyst,
            async_execution=True,
            expected_output= "Your final answer should be a comprehensive report on the student's challenges, backed by the data provided."
        )
    
    def opportunities_analysis_task(self, opportunities_analyst, academic_scores, study_profile, cognitive_inputs, context):
        return Task(
            description=dedent(f"""
                Based on the strengths and challenges reports, analyse and find the potential opportunities the student has based on his/her academic confidence scores, study profile and cognitive questionnaire responses.
                This task involves analysing each question-response pair given to you, then comparing with the benchmark data provided and finally identifying characteristics like:
                - what topics he/she is displaying medium confidence in, and and can be improved to score good marks.
                - if the student is average to good in a certain topic and if that topic has medium to high weightage (based on benchmark data), then consider it as a potential opportunity that can be achieved.
                - what study behaviour he/she can improve or acquire that can help her pursue her opportunities.
                - what cognitive thinking/mindset the student can acquire to help her mentally towards her opportunities.
            
                Academic Confidence Scores:
                    Physics:
                    {SCOAHelpers.format_scores(academic_scores['physics'])}
                        
                    Chemistry:
                    {SCOAHelpers.format_scores(academic_scores['chemistry'])}
                        
                    Mathematics:
                    {SCOAHelpers.format_scores(academic_scores['maths'])}
                    
                Study Profile:
                {SCOAHelpers.format_qa_pairs(study_profile)}
                    
                Cognitive Inputs:
                {SCOAHelpers.format_qa_pairs(cognitive_inputs)}
                    
                Based on this information, provide a detailed report of the student's potential opportunities.
                Suggest opportunities where the student can work on to improve their score.
                
                {SCOAHelpers.bonus_section()}
            """),
            agent=opportunities_analyst,
            async_execution=True,
            context=context,
            expected_output= "Your final answer should be a comprehensive report on the student's potential opportunities, backed by the data provided."
        )
    
    def actionables_analysis_task(self, actionables_analyst, context):
        return Task(
            description=dedent(f"""
                Based on the strengths, challenges and opportunities reports, device the best actionables the student has to take on his/her academic confidence scores, study profile and cognitive questionnaire responses.
                This task involves analysing all the three reports and preparing actionables like:
                - suggest what topics or subjects needs to be improved, along with the best study behaviour and cognitive changes the student should inculcate.
                - identify easy topics and suggest how the student can learn quickly to improve his score.
                - suggest the best strategy to tackle important topics the student is weak at, based on the student's study and cognitive profile.
            """),
            agent=actionables_analyst,
            async_execution=True,
            context=context,
            expected_output="Your final answer should be a practical and be relevant to the student's profile."
        )
    

class SCOAHelpers:
    @staticmethod
    def bonus_section():
        return "If you do your BEST WORK, I'll give you a bonus of ₹10000!"
    
    @staticmethod
    def format_scores(scores):
        return "\n".join([f"- {topic}: {score}" for topic, score in scores.items()])
    
    @staticmethod
    def format_qa_pairs(qa_dict):
        formatted_pairs = []
        for key, value in qa_dict.items():
            question = SCOAHelpers.get_question(key)
            formatted_pairs.append(f"Q: {question}\nA: {value}")
        return "\n\n".join(formatted_pairs)
    
    @staticmethod
    def get_question(key):
        questions = {
            'time_division': "How do you divide your study time among Physics, Chemistry and Mathematics for JEE? (Allocate Percentage)",
            'mock_test_frequency': "How often do you use mock tests and past question papers for JEE preparation?",
            'progress_monitoring': "How do you monitor your progress in JEE topics or chapters?",
            'study_methods': "How do you adjust your study methods for difficult or new JEE topics?",
            'study_techniques': "What techniques do you use to remember JEE concepts and formulas for a long time? eg: Revise frequently, Mindmap, etc.",
            'problem_solving_approach': "When faced with complex, multi-step problems in JEE, how likely are you to approach problem-solving systematically, breaking down each step?",
            'thorough_understanding': "In your JEE preparation, how likely are you to ensure thorough understanding of fundamental concepts before moving on to advanced topics?",
            'feedback': "How likely are you to integrate feedback from practice tests or teachers into your JEE preparation strategy?",
            'misconception': "When encountering a misconception or misunderstanding in a JEE concept, how likely are you to identify and resolve it?",
            'time_management': "How likely are you to effectively manage time during JEE exams, especially in sections with limited time constraints?"
        }
        return questions.get(key, "Question not found")