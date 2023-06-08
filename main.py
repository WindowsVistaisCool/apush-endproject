from manim import *

class SceneHelpers:
    class Anims:
        @staticmethod
        def integrator(s, animClass, mobject, **kwargs):
            return lambda: s.play(animClass(mobject, **kwargs))

        @staticmethod
        def fontIntegrator(s, a, text_mobject_creator, font_file, **kwargs):
            with register_font(font_file):
                mobject = text_mobject_creator(font_file.split('.')[0])
                return (SceneHelpers.Anims.integrator(s, a, mobject, **kwargs), mobject)

class IntroScene(MovingCameraScene):
    def construct(self):
        tcallable1, tobj1 = SceneHelpers.Anims.fontIntegrator(self, AddTextLetterByLetter,
            lambda font: Text("Terrorist Attacks", font=font).scale(1.5).shift(UP*1.5),
            "Bohemian Typewriter.ttf")
        tcallable1()
        SceneHelpers.Anims.fontIntegrator(self, AddTextLetterByLetter,
            lambda font: Text("on ur mom", font=font).scale(1.5).next_to(tobj1, DOWN),
            "Bohemian Typewriter.ttf")[0]()
        self.wait(0.4)
        SceneHelpers.Anims.fontIntegrator(self, Write,
            lambda font: Text("By Kyle Rush", font=font).scale(0.8).shift(DOWN*0.8),
            "Sirukota.ttf")[0]()
        SceneHelpers.Anims.integrator(self, FadeIn,
            Text("A Manim Animation").scale(0.5).align_on_border(DR*0.8),
            shift=DR*2, scale=2)()
        self.wait(1)

        self.play(self.camera.frame.animate.shift(DOWN*8), run_time=2)
        self.wait(0.25)

class TimelineViewScene(MovingCameraScene):
    def construct(self):
        sf_master = 0.85
        box_dimensions = (2.5, 1)
        arrow_buff = 0.6

        current_mobjects = VGroup()
        b1 = RoundedRectangle(0.25, height=box_dimensions[1], width=box_dimensions[0]).align_on_border(UL).shift(RIGHT*0.5 + DOWN*0.5).scale(sf_master)
        b1t = Text("1979").move_to(b1.get_center()).scale(sf_master)
        current_mobjects.add(b1, b1t)
        b2 = RoundedRectangle(0.25, height=box_dimensions[1], width=box_dimensions[0]).next_to(b1, RIGHT*10).scale(sf_master)
        b2t = Text("1988").move_to(b2.get_center()).scale(sf_master)
        connection1_2 = Arrow(b1t.get_right(), b2t.get_left(), buff=arrow_buff).scale(sf_master)
        b3 = RoundedRectangle(0.25, height=box_dimensions[1], width=box_dimensions[0]).next_to(b2, RIGHT*10).scale(sf_master)
        b3t = Text("1993").move_to(b3.get_center()).scale(sf_master)
        connection2_3 = Arrow(b2t.get_right(), b3t.get_left(), buff=arrow_buff).scale(sf_master)

        b4 = RoundedRectangle(0.25, height=box_dimensions[1], width=box_dimensions[0]).next_to(b1, DOWN*5).scale(sf_master)
        b4t = Text("1998").move_to(b4.get_center()).scale(sf_master)
        connection3_4 = Arrow(b3t.get_bottom(), b4t.get_top(), buff=arrow_buff).scale(sf_master)
        b5 = RoundedRectangle(0.25, height=box_dimensions[1], width=box_dimensions[0]).next_to(b4, RIGHT*10).scale(sf_master)
        b5t = Text("2000").move_to(b5.get_center()).scale(sf_master)
        connection4_5 = Arrow(b4t.get_right(), b5t.get_left(), buff=arrow_buff).scale(sf_master)
        b6 = RoundedRectangle(0.25, height=box_dimensions[1] + 0.5, width=10).align_on_border(DOWN).shift(UP*0.5).scale(sf_master)
        b6t = Text("September 11th, 2001").move_to(b6.get_center()).scale(sf_master + 0.2)
        connection5_6 = Arrow(b5t.get_bottom(), b6t.get_top(), buff=arrow_buff).scale(sf_master + 0.1)

        self.play(FadeIn(b1), Create(b1))
        self.play(FadeIn(b1t), AddTextLetterByLetter(b1t))
        self.wait()

        # B1 subanimation
        self.play(FadeOut(current_mobjects), self.camera.frame.animate.scale(0.5).move_to(b1.get_center()))
        self.camera.frame.scale(2).move_to(ORIGIN) # tricking viewer into new animation

        b1_subanimation_rawtext = "From 1979 to 1989, the Soviet Union invaded Afghanistan to support communism. The United States supported and aided the Mujahideen, who also opposed communism. While the Soviet Union eventually withdrew, the rise of Al-Qaeda would start which would shape conflicts globally."
        b1_subanimation_t = Text(b1_subanimation_rawtext[:67]).scale(0.5).shift(UP*2.5)
        b1_subanimation_t1 = Text(b1_subanimation_rawtext[67:136]).scale(0.5).next_to(b1_subanimation_t, DOWN)
        b1_subanimation_t2 = Text(b1_subanimation_rawtext[136:208]).scale(0.5).next_to(b1_subanimation_t1, DOWN)
        b1_subanimation_t3 = Text(b1_subanimation_rawtext[208:]).scale(0.5).next_to(b1_subanimation_t2, DOWN)
        b1_subanimation = VGroup(b1_subanimation_t, b1_subanimation_t1, b1_subanimation_t2, b1_subanimation_t3)

        for text in [b1_subanimation_t, b1_subanimation_t1, b1_subanimation_t2, b1_subanimation_t3]:
            self.play(AddTextLetterByLetter(text, run_time=2))

        self.wait(3)

        self.play(FadeOut(b1_subanimation))
        self.camera.frame.scale(0.25).move_to(b1.get_center())
        self.play(FadeIn(current_mobjects), self.camera.frame.animate.scale(4).move_to(ORIGIN))
        # End B1 subanimation

        self.play(GrowArrow(connection1_2), FadeIn(b2), Create(b2))
        self.play(FadeIn(b2t), AddTextLetterByLetter(b2t))
        current_mobjects.add(b2, b2t, connection1_2)
        self.wait()

        # B2 subanimation
        self.play(FadeOut(current_mobjects), self.camera.frame.animate.scale(0.5).move_to(b2.get_center()))
        self.camera.frame.scale(2).move_to(ORIGIN) # tricking viewer into new animation
        self.remove(b2, b2t, connection1_2)

        b2_subanimation_picture = ImageMobject("bin.jpg").scale(0.75).align_on_border(DOWN).shift(UP*0.4)
        self.play(FadeIn(b2_subanimation_picture))

        b2_subanimation_rawtext = "In 1988, a wealthy Saudi Arabian Merchant named Osama bin Laden formed Al-Qaeda, an extremist Islamist Organization. He sought to unite the world against enimies of Islam, in particular the United States. To achive its goals, Al-Qaeda expanded its operations into other countries and trained recruits in terrorist tactics which were employed heavily."
        b2_subanimation_t = Text(b2_subanimation_rawtext[:70]).scale(0.5).shift(UP*2.5)
        b2_subanimation_t1 = Text(b2_subanimation_rawtext[70:140]).scale(0.5).next_to(b2_subanimation_t, DOWN)
        b2_subanimation_t2 = Text(b2_subanimation_rawtext[140:215]).scale(0.5).next_to(b2_subanimation_t1, DOWN)
        b2_subanimation_t3 = Text(b2_subanimation_rawtext[215:284]).scale(0.5).next_to(b2_subanimation_t2, DOWN)
        b2_subanimation_t4 = Text(b2_subanimation_rawtext[284:]).scale(0.5).next_to(b2_subanimation_t3, DOWN)
        b2_subanimation = VGroup(b2_subanimation_t, b2_subanimation_t1, b2_subanimation_t2, b2_subanimation_t3, b2_subanimation_t4)

        for text in [b2_subanimation_t, b2_subanimation_t1, b2_subanimation_t2, b2_subanimation_t3, b2_subanimation_t4]:
            self.play(AddTextLetterByLetter(text, run_time=2))

        self.wait(3.5)

        self.play(FadeOut(b2_subanimation, b2_subanimation_picture))
        self.camera.frame.scale(0.25).move_to(b2.get_center())
        self.play(FadeIn(current_mobjects), self.camera.frame.animate.scale(4).move_to(ORIGIN))
        # End B2 subanimation

        self.play(GrowArrow(connection2_3), FadeIn(b3), Create(b3))
        self.play(FadeIn(b3t), AddTextLetterByLetter(b3t))
        current_mobjects.add(b3, b3t, connection2_3)
        self.wait()

        # B3 subanimation
        self.play(FadeOut(current_mobjects), self.camera.frame.animate.scale(0.25).move_to(b3.get_center()))
        self.camera.frame.scale(4).move_to(ORIGIN) # tricking viewer into new animation
        self.remove(b3, b3t, connection2_3)

        b3_subanimation_picture = ImageMobject("wtc1993.jpg").scale(1.75).align_on_border(DOWN).shift(LEFT*4 + UP*0.3)
        b3_subanimation_picture2 = ImageMobject("wtc19932.jpg").scale(0.65).next_to(b3_subanimation_picture, RIGHT*14)
        self.play(FadeIn(b3_subanimation_picture, b3_subanimation_picture2))

        b3_subanimation_rawtext = "In 1993, a truck was detonated in front of the parking garage in the North Tower of the World Trade Center by Al-Qaeda. It was intended to topple both towers, however both still remained but many were injured."
        b3_subanimation_t = Text(b3_subanimation_rawtext[:69]).scale(0.5).shift(UP*2.5)
        b3_subanimation_t1 = Text(b3_subanimation_rawtext[69:146]).scale(0.5).next_to(b3_subanimation_t, DOWN)
        b3_subanimation_t2 = Text(b3_subanimation_rawtext[146:]).scale(0.5).next_to(b3_subanimation_t1, DOWN)
        b3_subanimation = VGroup(b3_subanimation_t, b3_subanimation_t1, b3_subanimation_t2)

        for text in [b3_subanimation_t, b3_subanimation_t1, b3_subanimation_t2]:
            self.play(AddTextLetterByLetter(text, run_time=2))

        self.wait(2.75)

        self.play(FadeOut(b3_subanimation, b3_subanimation_picture, b3_subanimation_picture2))
        self.camera.frame.scale(0.25).move_to(b3.get_center())
        self.play(FadeIn(current_mobjects), self.camera.frame.animate.scale(4).move_to(ORIGIN))
        # End B3 subanimation

        self.play(GrowArrow(connection3_4), FadeIn(b4), Create(b4))
        self.play(FadeIn(b4t), AddTextLetterByLetter(b4t))
        current_mobjects.add(b4, b4t, connection3_4)
        self.wait()

        # B4 subanimation
        self.play(FadeOut(current_mobjects), self.camera.frame.animate.scale(0.25).move_to(b4.get_center()))
        self.camera.frame.scale(4).move_to(ORIGIN) # tricking viewer into new animation
        self.remove(b4, b4t, connection3_4)

        b4_subanimation_picture = ImageMobject("embassy_1.jpg").scale(0.3).align_on_border(DOWN).shift(UP*0.2)
        self.play(FadeIn(b4_subanimation_picture))

        b4_subanimation_rawtext = "In 1998, Al-Qaeda simultaneously carried out bombings on multiple US embassies in Africa. These attacks resulted in deaths of hundreds and were a significant demonstration of global power of Al-Qaeda's terrorism. It also shows how the US is being targeted by them the most and heightened concerns on this major threat."
        b4_subanimation_t = Text(b4_subanimation_rawtext[:69]).scale(0.5).shift(UP*2.5)
        b4_subanimation_t1 = Text(b4_subanimation_rawtext[69:145]).scale(0.5).next_to(b4_subanimation_t, DOWN)
        b4_subanimation_t2 = Text(b4_subanimation_rawtext[145:213]).scale(0.5).next_to(b4_subanimation_t1, DOWN)
        b4_subanimation_t3 = Text(b4_subanimation_rawtext[213:288]).scale(0.5).next_to(b4_subanimation_t2, DOWN)
        b4_subanimation_t4 = Text(b4_subanimation_rawtext[288:]).scale(0.5).next_to(b4_subanimation_t3, DOWN)
        b4_subanimation = VGroup(b4_subanimation_t, b4_subanimation_t1, b4_subanimation_t2, b4_subanimation_t3, b4_subanimation_t4)

        for text in [b4_subanimation_t, b4_subanimation_t1, b4_subanimation_t2, b4_subanimation_t3, b4_subanimation_t4]:
            self.play(AddTextLetterByLetter(text, run_time=2))

        self.wait(4.5)

        self.play(FadeOut(b4_subanimation, b4_subanimation_picture))
        self.camera.frame.scale(0.25).move_to(b4.get_center())
        self.play(FadeIn(current_mobjects), self.camera.frame.animate.scale(4).move_to(ORIGIN))
        # End B4 subanimation

        self.play(GrowArrow(connection4_5), FadeIn(b5), Create(b5))
        self.play(FadeIn(b5t), AddTextLetterByLetter(b5t))
        current_mobjects.add(b5, b5t, connection4_5)
        self.wait()

        # B5 subanimation
        self.play(FadeOut(current_mobjects), self.camera.frame.animate.scale(0.25).move_to(b5.get_center()))
        self.camera.frame.scale(4).move_to(ORIGIN) # tricking viewer into new animation
        self.remove(b5, b5t, connection4_5)

        b5_subanimation_picture = ImageMobject("usscole.jpg").scale(0.3).align_on_border(DOWN).shift(UP*0.2)
        self.play(FadeIn(b5_subanimation_picture))

        b5_subanimation_rawtext = "In 2000, US navy destroyer USS Cole was bombed in Yemen by Al-Qaeda. Many died on the ship due to the explosives on a smaller boat exploding near the ship which also caused the vessel significant damage. This shows how Al-Qaeda was targetting US military and further highlighted the need for security."
        b5_subanimation_t = Text(b5_subanimation_rawtext[:69]).scale(0.5).shift(UP*2.5)
        b5_subanimation_t1 = Text(b5_subanimation_rawtext[69:140]).scale(0.5).next_to(b5_subanimation_t, DOWN)
        b5_subanimation_t2 = Text(b5_subanimation_rawtext[140:215]).scale(0.5).next_to(b5_subanimation_t1, DOWN)
        b5_subanimation_t3 = Text(b5_subanimation_rawtext[215:283]).scale(0.5).next_to(b5_subanimation_t2, DOWN)
        b5_subanimation_t4 = Text(b5_subanimation_rawtext[283:]).scale(0.5).next_to(b5_subanimation_t3, DOWN)
        b5_subanimation = VGroup(b5_subanimation_t, b5_subanimation_t1, b5_subanimation_t2, b5_subanimation_t3, b5_subanimation_t4)

        for text in [b5_subanimation_t, b5_subanimation_t1, b5_subanimation_t2, b5_subanimation_t3, b5_subanimation_t4]:
            self.play(AddTextLetterByLetter(text, run_time=2))

        self.wait(4.5)

        self.play(FadeOut(b5_subanimation, b5_subanimation_picture))
        self.camera.frame.scale(0.25).move_to(b5.get_center())
        self.play(FadeIn(current_mobjects), self.camera.frame.animate.scale(4).move_to(ORIGIN))
        # End B5 subanimation
        
        self.play(GrowArrow(connection5_6), FadeIn(b6), Create(b6))
        self.play(FadeIn(b6t), AddTextLetterByLetter(b6t))
        current_mobjects.add(b6, b6t, connection5_6)
        self.wait()

        # B6 subanimation
        self.play(FadeOut(current_mobjects), self.camera.frame.animate.scale(0.5).move_to(b6.get_center()))
        self.camera.frame.scale(2).move_to(ORIGIN) # tricking viewer into new animation
        self.remove(b6, b6t, connection5_6)

        b6_subanimation_image = ImageMobject('towers.jpg').scale(6.5)
        self.bring_to_back(b6_subanimation_image)

        b6_subanimation_plane = ImageMobject('plane.jpg').scale(0.8).shift(RIGHT).shift(UP*0.4)
        b6_subanimation_fire = ImageMobject('fire.png').scale(0.25).shift(LEFT*2.75).shift(UP*1.75)

        self.add(b6_subanimation_image)
        self.add(b6_subanimation_plane)
        self.wait()
        self.play(b6_subanimation_plane.animate.shift(LEFT*4).shift(UP*1.75).rotate(PI/2).scale(0.5))
        self.remove(b6_subanimation_plane)
        self.add(b6_subanimation_fire)
        self.wait(2)

        self.play(FadeOut(b6_subanimation_image, b6_subanimation_plane, b6_subanimation_fire))

        b6_subanimation2_rawtext = "On September 11, 2001, a series of coordinated terrorist attacks were carried out by Al-Qaeda on the United States. Nineteen hijackers, primarily from Saudi Arabia, seized control of four commercial airliners. They deliberately crashed two planes into the Twin Towers of the World Trade Center in New York City, causing both towers to collapse. Another plane was flown into the Pentagon in Arlington, Virginia, while the fourth plane crashed into a field in Pennsylvania after passengers attempted to regain control from the hijackers. The attacks resulted in the deaths of nearly 3,000 people, including passengers, office workers, and emergency responders. This event had a profound impact on national security, leading to significant changes in counterterrorism efforts and security in the United States."
        b6_subanimation2_t = Text(b6_subanimation2_rawtext[:70]).scale(0.5).shift(UP*3)
        b6_subanimation2_t1 = Text(b6_subanimation2_rawtext[70:146]).scale(0.5).next_to(b6_subanimation2_t, DOWN)
        b6_subanimation2_t2 = Text(b6_subanimation2_rawtext[146:210]).scale(0.5).next_to(b6_subanimation2_t1, DOWN)
        b6_subanimation2_t3 = Text(b6_subanimation2_rawtext[210:280]).scale(0.5).next_to(b6_subanimation2_t2, DOWN)
        b6_subanimation2_t4 = Text(b6_subanimation2_rawtext[280:353]).scale(0.5).next_to(b6_subanimation2_t3, DOWN)
        b6_subanimation2_t5 = Text(b6_subanimation2_rawtext[353:420]).scale(0.5).next_to(b6_subanimation2_t4, DOWN)
        b6_subanimation2_t6 = Text(b6_subanimation2_rawtext[420:488]).scale(0.5).next_to(b6_subanimation2_t5, DOWN)
        b6_subanimation2_t7 = Text(b6_subanimation2_rawtext[488:560]).scale(0.5).next_to(b6_subanimation2_t6, DOWN)
        b6_subanimation2_t8 = Text(b6_subanimation2_rawtext[560:632]).scale(0.5).next_to(b6_subanimation2_t7, DOWN)
        b6_subanimation2_t9 = Text(b6_subanimation2_rawtext[632:704]).scale(0.5).next_to(b6_subanimation2_t8, DOWN)
        b6_subanimation2_t10 = Text(b6_subanimation2_rawtext[704:773]).scale(0.5).next_to(b6_subanimation2_t9, DOWN)
        b6_subanimation2_t11 = Text(b6_subanimation2_rawtext[773:]).scale(0.5).next_to(b6_subanimation2_t10, DOWN)
        b6_subanimation2 = VGroup(b6_subanimation2_t, b6_subanimation2_t1, b6_subanimation2_t2, b6_subanimation2_t3, b6_subanimation2_t4, b6_subanimation2_t5, b6_subanimation2_t6, b6_subanimation2_t7, b6_subanimation2_t8, b6_subanimation2_t9, b6_subanimation2_t10, b6_subanimation2_t11)

        for text in [b6_subanimation2_t, b6_subanimation2_t1, b6_subanimation2_t2, b6_subanimation2_t3, b6_subanimation2_t4, b6_subanimation2_t5, b6_subanimation2_t6, b6_subanimation2_t7, b6_subanimation2_t8, b6_subanimation2_t9, b6_subanimation2_t10, b6_subanimation2_t11]:
            self.play(AddTextLetterByLetter(text, run_time=2))
        
        self.wait(8)

        self.play(FadeOut(b6_subanimation2))
        self.camera.frame.scale(0.5).move_to(b6.get_center())
        self.play(FadeIn(current_mobjects), self.camera.frame.animate.scale(2).move_to(ORIGIN))
        # End B6 subanimation

        self.wait()