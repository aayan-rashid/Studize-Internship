from crewai import Task

class RoadmapTasks():
    def sentiment_analysis(self, agent, user_input):
        return Task(
            description='Analyze the students academic, cognitive and personal profile and set the mood/sentiment by doing an in-depth for the Roadmap in context to the JEE Mains exam.',
            agent=agent,
            user_input=user_input,
            async_execution=True,
        )




    def high_level_plan(self, agent, context):
        return Task(
            description='Create a high-level phase-wise Roadmap that has the contents divided into phases of 2 months each that will serve as a high level plan or approach that will be undertaken by the student to prepare for the JEE examination. Pass on the plan for each month separately to the monthly agent',
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
            description='Create a month-wise plan for each phase that divides the goals into 4 weeks of the month',
            agent=agent,
            context=context,
            async_execution=True,

            expected_output="""Expand each month wise description into a 4 week plan.
                Example output for 1 month, but while generation create 4 week plans for each month in the high level plan.:

                * Week 1:
                    + Maths: Complete basics of Algebra (Quadratic Equations, Sequence and Series, Permutations and Combinations)
                    + Chemistry: Finish basics of Physical Chemistry (Atomic Structure, States of Matter, Thermodynamics)
                    + Physics: Complete basics of Mechanics (Motion, Thermodynamics, Oscillations and Waves)
                * Week 2:
                    + Maths: Focus on Trigonometry (Trigonometric Equations, Properties of Triangles)
                    + Chemistry: Study Inorganic Chemistry (Chemical Bonding, Coordination Compounds, Salt Analysis)
                    + Physics: Cover Electricity (Electrostatics, Electric Current, Resistance)

                * Week 3:
                    + Maths: Focus on Coordinate Geometry (Circles, Conic Sections) and Calculus (Limits and Continuity)
                    + Chemistry: Study Organic Chemistry (Aldehydes and Ketones, Aromatic Hydrocarbons, GOC Isomerism)
                    + Physics: Cover Magnetism (Magnetism, Electromagnetic Induction)
                * Week 4:
                    + Maths: Focus on Vectors and 3D Geometry
                    + Chemistry: Study Electrochemistry and Biomolecules
                    + Physics: Cover Optics (Reflection, Refraction, Lenses)
                """,
        )
        
    

    def week_level_plan(self, weekly_agent, context):
        return Task(
            description = 'Based on the weekwise plan provided, generate a detailed daywise plan for the entire week by giving a structured set of tasks (topics, subtopics and particular problems) to be completed, and divide those tasks in a daywise manner for the week.',
            agent=weekly_agent,
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

                * Review and Revision
                    + Review notes and practice problems on all subjects
                    + Revise weak areas and practice more questions
            """
        )
        

    
    
    def compile_roadmap(self, agent, context, callback_function):
        return Task(
            description='Compile the entire roadmap into a final roadmap.',
            agent=agent,
            context=context,
            async_execution=True,

            expected_output="""Create for each month a compiled roadmap 
                Example Output:
                **Month 1 (Current Month): Fundamentals and Basics (Maths, Chemistry, and Physics)**

                **Week 1:** 
                    **Goals:** 
                        - Physics: Complete the topics of Kinematics and Laws of Motion, with a focus on
                        understanding the concepts and solving numerical problems.
                        - Chemistry: Finish the topics of Atomic Structure and Periodic Table, with an emphasis on
                        understanding the periodic trends and properties of elements.
                        - Mathematics: Complete the topics of Sets, Relations, and Functions, with a focus on
                        understanding the concepts and solving problems.

                    **Monday:**
                        **Tasks:**
                            + 3 hours of Physics study time (Mechanics - Kinematics)
                            + 1 hour of review and practice
                        **Time-Table:**
                            * 9:00 AM - 10:30 AM: Physics - Motion in a Straight Line (1.5 hours)
                            * 10:30 AM - 12:00 PM: Break
                            * 12:00 PM - 1:30 PM: Chemistry - Atomic Structure (1.5 hours)
                            * 1:30 PM - 2:30 PM: Break
                            * 2:30 PM - 4:00 PM: Mathematics - Sets, Relations, and Functions (1.5 hours)
                            * 4:00 PM - 5:00 PM: Review and practice previous week's topics (1 hour)

                    **Tuesday:**
                        **Tasks:**
                            + 2 hours of Physics study time (Mechanics - Dynamics)
                            + 1 hour of review and practice
                        **Time-Table:**
                            * 9:00 AM - 10:30 AM: Physics - Motion in a Plane (1.5 hours)
                            * 10:30 AM - 12:00 PM: Break
                            * 12:00 PM - 1:30 PM: Chemistry - Chemical Bonding (1.5 hours)
                            * 1:30 PM - 2:30 PM: Break
                            * 2:30 PM - 4:00 PM: Practice 50 questions from Physics (1.5 hours)
                            * 4:00 PM - 5:00 PM: Review and practice previous week's topics (1 hour)

                    **Wednesday:**
                        **Tasks:**
                            + 3 hours of Physics study time (Mechanics - Rotational Motion)
                            + 1 hour of review and practice
                        **Time-Table:**
                            * 9:00 AM - 10:30 AM: Physics - Motion in a Straight Line (1.5 hours)
                            * 10:30 AM - 12:00 PM: Break
                            * 12:00 PM - 1:30 PM: Chemistry - Atomic Structure (1.5 hours)
                            * 1:30 PM - 2:30 PM: Break
                            * 2:30 PM - 4:00 PM: Mathematics - Sets, Relations, and Functions (1.5 hours)
                            * 4:00 PM - 5:00 PM: Review and practice previous week's topics (1 hour)

                    **Thursday:**
                        **Tasks:**
                            + 2 hours of Physics study time (Mechanics - Work and Energy)
                            + 1 hour of review and practice
                        **Time-Table:**
                            * 9:00 AM - 10:30 AM: Physics - Motion in a Straight Line (1.5 hours)
                            * 10:30 AM - 12:00 PM: Break
                            * 12:00 PM - 1:30 PM: Chemistry - Atomic Structure (1.5 hours)
                            * 1:30 PM - 2:30 PM: Break
                            * 2:30 PM - 4:00 PM: Mathematics - Sets, Relations, and Functions (1.5 hours)
                            * 4:00 PM - 5:00 PM: Review and practice previous week's topics (1 hour)

                    **Friday:**
                        **Tasks:**
                            + 3 hours of Physics study time (Mechanics - Review and Practice)
                            + 1 hour of review and practice
                        **Time-Table:**
                            * 9:00 AM - 10:30 AM: Physics - Motion in a Straight Line (1.5 hours)
                            * 10:30 AM - 12:00 PM: Break
                            * 12:00 PM - 1:30 PM: Chemistry - Atomic Structure (1.5 hours)
                            * 1:30 PM - 2:30 PM: Break
                            * 2:30 PM - 4:00 PM: Mathematics - Sets, Relations, and Functions (1.5 hours)
                            * 4:00 PM - 5:00 PM: Review and practice previous week's topics (1 hour)

                    **Saturday:**
                        **Tasks:**
                            + 4 hour of review and practice of Physics
                            + 4 hour review and practice of Maths
                            + 4 hours review and practice of Chemistry
                        **Time-Table:**
                            * 7:00 AM - 11:00 AM: Review and practice previous week's topics of Physics(4 hours)
                            * 11:00 AM - 12:00 PM: Break
                            * 12:00 PM - 4:00 PM: Review and practice previous week's topics of Chemistry(4 hours)
                            * 4:00 PM - 6:00 PM: Break
                            * 6:00 PM - 10:00 PM: Review and practice previous week's topics of Maths(4 hours)
                            * 10:00 PM - 11:00 PM: Break

                    **Sunday:**
                        **Tasks:**
                            + 4 hour of review and practice of Physics
                            + 4 hour review and practice of Maths
                            + 4 hours review and practice of Chemistry
                        **Time-Table:**
                            * 7:00 AM - 11:00 AM: Review and practice previous week's topics of Physics(4 hours)
                            * 11:00 AM - 12:00 PM: Break
                            * 12:00 PM - 4:00 PM: Review and practice previous week's topics of Chemistry(4 hours)
                            * 4:00 PM - 6:00 PM: Break
                            * 6:00 PM - 10:00 PM: Review and practice previous week's topics of Maths(4 hours)
                            * 10:00 PM - 11:00 PM: Break            
            """,

            callback=callback_function
        )

        