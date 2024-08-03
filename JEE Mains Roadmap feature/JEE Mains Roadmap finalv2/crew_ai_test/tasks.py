from crewai import Task

class RoadmapTasks():
    def high_level_plan(self, agent, context):
        return Task(
            description="Based on the information regarding the JEE Mains topics in each subject, their respective weightages and important subtopics, create a high level plan for one year, providing a roadmap for JEE Mains preparation in phases or months that will serve as a high level plan or approach that will be undertaken by the student to prepare for the JEE examination. Pass on each month separately to the monthly agent",
            agent=agent,
            context=context,
            async_execution=True,
            expected_output="""A high level plan, divided into monthwise phases (based on the time left for the student for preparation) and bulletted description for each phase depicting what the monthly planner agent will further need to focus on to create week wise plans
            Example Output:
            **Phase 1: Month 1-2 - Fundamentals and Basics (Maths, Chemistry, and Physics)**

            * Month 1:
                + Maths: Complete basics of Algebra, Trigonometry, and Coordinate Geometry
                + Chemistry: Finish basics of Physical Chemistry, Inorganic Chemistry, and Organic Chemistry
                + Physics: Complete basics of Mechanics, Thermodynamics, and Oscillations
            * Month 2:
                + Maths: Focus on Calculus, Vectors, and 3D Geometry
                + Chemistry: Study Chemical Bonding, Stoichiometry, and Periodic Table
                + Physics: Cover Electricity, Magnetism, and Electromagnetic Induction

            **Phase 2: Month 3-4 - Building Concepts (Maths, Chemistry, and Physics)**

            * Month 3:
                + Maths: Focus on Differential Equations, Probability, and Statistics
                + Chemistry: Study Organic Chemistry, Biomolecules, and Environmental Chemistry
                + Physics: Cover Optics, Modern Physics, and Semiconductor Electronics
            * Month 4:
                + Maths: Complete Number Systems, Quadratic Equations, and Inequalities
                + Chemistry: Focus on Coordination Compounds, Chemical Kinetics, and Surface Chemistry
                + Physics: Study Rotational Motion, Gravitation, and Waves

            **Phase 3: Month 5-6 - Practice and Revision (Maths, Chemistry, and Physics)**

            * Month 5:
                + Practice mock tests and previous year's question papers
                + Revise weak areas and focus on improving speed and accuracy
            * Month 6:
                + Take full-length mock tests and analyze performance
                + Focus on improving weak areas and building endurance

            **Phase 4: Month 7-12 - Intensive Practice and Revision (Maths, Chemistry, and Physics)**

            * Month 7-9:
                + Take regular mock tests and practice previous year's question papers
                + Focus on improving weak areas and building speed and accuracy
            * Month 10-12:
                + Take full-length mock tests and analyze performance
                + Focus on building endurance and improving weak areas
            """
        )
    
    def month_level_plan(self, agent, context):
        return Task(
            description="Generating a 4 week plan for each month in the high level plan, where the student is studying 40 hours per week. Each must be a detailed to-do list such that the 4 weeks combined achieve the month target in the high level plan. Generate 4 week plans for each month in the high level plan in detail. The agent should be able to use the tool provided to look up the topics/subtopics of the chapters listed in the month description in the high level plan and creak week wise plans for those months accordingly",
            agent=agent,
            async_execution=True,
            context=context,
            expected_output="""Expand each month wise description into a 4 week plan.
            Example output for 1 month, but while generation create 4 week plans for each month in the high level plan.:
            **Week 1-2: Fundamentals and Basics (Maths, Chemistry, and Physics)**

            * Week 1:
                + Maths: Complete basics of Algebra (Quadratic Equations, Sequence and Series, Permutations and Combinations)
                + Chemistry: Finish basics of Physical Chemistry (Atomic Structure, States of Matter, Thermodynamics)
                + Physics: Complete basics of Mechanics (Motion, Thermodynamics, Oscillations and Waves)
            * Week 2:
                + Maths: Focus on Trigonometry (Trigonometric Equations, Properties of Triangles)
                + Chemistry: Study Inorganic Chemistry (Chemical Bonding, Coordination Compounds, Salt Analysis)
                + Physics: Cover Electricity (Electrostatics, Electric Current, Resistance)

            **Week 3-4: Building Concepts (Maths, Chemistry, and Physics)**

            * Week 3:
                + Maths: Focus on Coordinate Geometry (Circles, Conic Sections) and Calculus (Limits and Continuity)
                + Chemistry: Study Organic Chemistry (Aldehydes and Ketones, Aromatic Hydrocarbons, GOC Isomerism)
                + Physics: Cover Magnetism (Magnetism, Electromagnetic Induction)
            * Week 4:
                + Maths: Focus on Vectors and 3D Geometry
                + Chemistry: Study Electrochemistry and Biomolecules
                + Physics: Cover Optics (Reflection, Refraction, Lenses)
            """
        )
        
    

    def week_level_plan(self, agent, context):
        return Task(
            description = "Based on the weekwise plan provided, generate a detailed daywise plan for the week by giving a structured set of tasks (topics, subtopics and particular problems) to be completed, and divide those tasks in a daywise manner for the week",
            agent=agent,
            async_execution=True,
            context=context,
            expected_output="""**Monday**

                * Maths: Coordinate Geometry (Circles)
                    + Study theory of circles (equations, properties, and applications)
                    + Practice problems: 10 questions on circles (5 easy, 3 medium, 2 hard)
                * Chemistry: Organic Chemistry (Aldehydes and Ketones)
                    + Study theory of aldehydes and ketones (structure, properties, and reactions)
                    + Practice problems: 5 questions on aldehydes and ketones (2 easy, 2 medium, 1 hard)
                * Physics: Magnetism
                    + Study theory of magnetism (magnetic fields, forces, and torque)
                    + Practice problems: 5 questions on magnetism (2 easy, 2 medium, 1 hard)

                **Tuesday**

                * Maths: Coordinate Geometry (Conic Sections)
                    + Study theory of conic sections (parabola, ellipse, and hyperbola)
                    + Practice problems: 10 questions on conic sections (5 easy, 3 medium, 2 hard)
                * Chemistry: Organic Chemistry (Aromatic Hydrocarbons)
                    + Study theory of aromatic hydrocarbons (structure, properties, and reactions)
                    + Practice problems: 5 questions on aromatic hydrocarbons (2 easy, 2 medium, 1 hard)
                * Physics: Electromagnetic Induction
                    + Study theory of electromagnetic induction (Faraday's law, Lenz's law)
                    + Practice problems: 5 questions on electromagnetic induction (2 easy, 2 medium, 1 hard)

                **Wednesday**

                * Maths: Calculus (Limits)
                    + Study theory of limits (concept, properties, and applications)
                    + Practice problems: 10 questions on limits (5 easy, 3 medium, 2 hard)
                * Chemistry: Organic Chemistry (GOC Isomerism)
                    + Study theory of GOC isomerism (structural isomerism, stereoisomerism)
                    + Practice problems: 5 questions on GOC isomerism (2 easy, 2 medium, 1 hard)
                * Physics: Revision of Magnetism and Electromagnetic Induction
                    + Revise notes and practice problems on magnetism and electromagnetic induction

                **Thursday**

                * Maths: Calculus (Continuity)
                    + Study theory of continuity (concept, properties, and applications)
                    + Practice problems: 10 questions on continuity (5 easy, 3 medium, 2 hard)
                * Chemistry: Revision of Organic Chemistry
                    + Revise notes and practice problems on aldehydes and ketones, aromatic hydrocarbons, and GOC isomerism
                * Physics: Revision of Physics
                    + Revise notes and practice problems on magnetism and electromagnetic induction

                **Friday**

                * Maths: Practice Test on Coordinate Geometry and Calculus
                    + Take a practice test on coordinate geometry and calculus (30 questions, 1 hour)
                * Chemistry: Practice Test on Organic Chemistry
                    + Take a practice test on organic chemistry (30 questions, 1 hour)
                * Physics: Practice Test on Physics
                    + Take a practice test on physicßs (30 questions, 1 hour)

                **Saturday**

                * Review and Revision
                    + Review notes and practice problems on all subjects
                    + Revise weak areas and practice more questions

                **Sunday**

                * Rest and Relaxation
                    + Take a break and relax to recharge for the next week
            """
        )
        

    def sentiment_analysis(self,agent):
        return Task(
            description="Given a Strengths, Opportunities, and Challenges analysis of a student, prepare a report summarizing the academic ability and the study behaviour of the student that can be further used to create a personalized roadmap for JEE Mains preparation",
            agent=agent,
            async_execution=True,
        )
    
    def compile_roadmap(self, agent, context):
        return Task(
            description='Compile all the weekly plans to generate the final roadmap',
            agent=agent,
            context=context,
            # expected_output="""**Week 1-2: Fundamentals and Basics (Maths, Chemistry, and Physics)**

            # * Week 1:
            #     + Maths: Complete basics of Algebra (Quadratic Equations, Sequence and Series, Permutations and Combinations)
            #     + Chemistry: Finish basics of Physical Chemistry (Atomic Structure, States of Matter, Thermodynamics)
            #     + Physics: Complete basics of Mechanics (Motion, Thermodynamics, Oscillations and Waves)
            # * Week 2:
            #     + Maths: Focus on Trigonometry (Trigonometric Equations, Properties of Triangles)
            #     + Chemistry: Study Inorganic Chemistry (Chemical Bonding, Coordination Compounds, Salt Analysis)
            #     + Physics: Cover Electricity (Electrostatics, Electric Current, Resistance)

            # **Week 3-4: Building Concepts (Maths, Chemistry, and Physics)**

            # * Week 3:
            #     + Maths: Focus on Coordinate Geometry (Circles, Conic Sections) and Calculus (Limits and Continuity)
            #     + Chemistry: Study Organic Chemistry (Aldehydes and Ketones, Aromatic Hydrocarbons, GOC Isomerism)
            #     + Physics: Cover Magnetism (Magnetism, Electromagnetic Induction)
            # * Week 4:
            #     + Maths: Focus on Vectors and 3D Geometry
            #     + Chemistry: Study Electrochemistry and Biomolecules
            #     + Physics: Cover Optics (Reflection, Refraction, Lenses)
            # """
        )

        

