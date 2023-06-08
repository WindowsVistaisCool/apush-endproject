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
        b2t = Text("1989").move_to(b2.get_center()).scale(sf_master)
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
        # self.wait()

        # B1 subanimation
        # self.play(FadeOut(current_mobjects), self.camera.frame.animate.scale(0.5).move_to(b1.get_center()))
        # self.camera.frame.scale(2).move_to(ORIGIN) # tricking viewer into new animation

        # b1_subanimation_t = Text("The United States supported Afghanistan in the Soviet-Afghan War.").scale(0.5).shift(UP*2.5)
        # b1_subanimation_t2 = Text("This would shape conflicts between the united states and other").scale(0.5).next_to(b1_subanimation_t, DOWN)
        # b1_subanimation = VGroup(b1_subanimation_t, b1_subanimation_t2)

        # self.play(AddTextLetterByLetter(b1_subanimation_t, run_time=2))
        # self.wait(0.4)
        # self.play(AddTextLetterByLetter(b1_subanimation_t2, run_time=2))
        # self.wait()

        # self.play(FadeOut(b1_subanimation))
        # self.camera.frame.scale(0.25).move_to(b1.get_center())
        # self.play(FadeIn(current_mobjects), self.camera.frame.animate.scale(4).move_to(ORIGIN))
        # End B1 subanimation

        self.play(GrowArrow(connection1_2), FadeIn(b2), Create(b2))
        self.play(FadeIn(b2t), AddTextLetterByLetter(b2t))
        current_mobjects.add(b2, b2t, connection1_2)
        # self.wait()

        # B2 subanimation
        # self.play(FadeOut(current_mobjects), self.camera.frame.animate.scale(0.5).move_to(b2.get_center()))
        # self.camera.frame.scale(2).move_to(ORIGIN) # tricking viewer into new animation

        # b2_subanimation_t = Text("embassy was bombed by mr al quadea himself!!").scale(0.5).shift(UP*2.5)
        # b2_subanimation_t1 = Text("people injured that not good lmao!!").scale(0.5).next_to(b2_subanimation_t, DOWN)
        # b2_subanimation = VGroup(b2_subanimation_t, b2_subanimation_t1)

        # self.play(AddTextLetterByLetter(b2_subanimation_t, run_time=2))
        # self.wait(0.4)
        # self.play(AddTextLetterByLetter(b2_subanimation_t1, run_time=2))
        # self.wait()

        # self.play(FadeOut(b2_subanimation))
        # self.camera.frame.scale(0.25).move_to(b2.get_center())
        # self.play(FadeIn(current_mobjects), self.camera.frame.animate.scale(4).move_to(ORIGIN))
        # End B2 subanimation

        self.play(GrowArrow(connection2_3), FadeIn(b3), Create(b3))
        self.play(FadeIn(b3t), AddTextLetterByLetter(b3t))
        current_mobjects.add(b3, b3t, connection2_3)
        # self.wait()

        # B3 subanimation
        # self.play(FadeOut(current_mobjects), self.camera.frame.animate.scale(0.25).move_to(b3.get_center()))
        # self.camera.frame.scale(4).move_to(ORIGIN) # tricking viewer into new animation

        # b3_subanimation_t = Text("its 2am and i don't even know what i'm doing anymore please help.").scale(0.5).shift(UP*2.5)
        # b3_subanimation_t1 = Text("i'm so tired and i just want to sleep").scale(0.5).next_to(b3_subanimation_t, DOWN)
        # b3_subanimation = VGroup(b3_subanimation_t, b3_subanimation_t1)

        # self.play(AddTextLetterByLetter(b3_subanimation_t, run_time=2))
        # self.wait(0.4)
        # self.play(AddTextLetterByLetter(b3_subanimation_t1, run_time=2))
        # self.wait()

        # self.play(FadeOut(b3_subanimation))
        # self.camera.frame.scale(0.25).move_to(b3.get_center())
        # self.play(FadeIn(current_mobjects), self.camera.frame.animate.scale(4).move_to(ORIGIN))
        # End B3 subanimation

        self.play(GrowArrow(connection3_4), FadeIn(b4), Create(b4))
        self.play(FadeIn(b4t), AddTextLetterByLetter(b4t))
        current_mobjects.add(b4, b4t, connection3_4)
        # self.wait()

        # B4 subanimation
        # self.play(FadeOut(current_mobjects), self.camera.frame.animate.scale(0.25).move_to(b4.get_center()))
        # self.camera.frame.scale(4).move_to(ORIGIN) # tricking viewer into new animation

        # b4_subanimation_t = Text("WAHHHHHHH").scale(4).shift(UP*2.5)
        # b4_subanimation_t1 = Text("please help im going insane").scale(0.5).next_to(b4_subanimation_t, DOWN)
        # b4_subanimation = VGroup(b4_subanimation_t, b4_subanimation_t1)

        # self.play(AddTextLetterByLetter(b4_subanimation_t, run_time=2))
        # self.wait(0.4)
        # self.play(AddTextLetterByLetter(b4_subanimation_t1, run_time=2))
        # self.wait()

        # self.play(FadeOut(b4_subanimation))
        # self.camera.frame.scale(0.25).move_to(b4.get_center())
        # self.play(FadeIn(current_mobjects), self.camera.frame.animate.scale(4).move_to(ORIGIN))
        # End B4 subanimation

        self.play(GrowArrow(connection4_5), FadeIn(b5), Create(b5))
        self.play(FadeIn(b5t), AddTextLetterByLetter(b5t))
        current_mobjects.add(b5, b5t, connection4_5)
        # self.wait()

        # B5 subanimation
        # End B5 subanimation

        self.play(GrowArrow(connection5_6), FadeIn(b6), Create(b6))
        self.play(FadeIn(b6t), AddTextLetterByLetter(b6t))
        current_mobjects.add(b6, b6t, connection5_6)
        # self.wait()

        # B6 subanimation
        self.play(FadeOut(current_mobjects), self.camera.frame.animate.scale(0.5).move_to(b6.get_center()))
        self.camera.frame.scale(2).move_to(ORIGIN) # tricking viewer into new animation

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
        self.camera.frame.scale(0.5).move_to(b6.get_center())
        self.play(FadeIn(current_mobjects), self.camera.frame.animate.scale(2).move_to(ORIGIN))
        # End B6 subanimation

        self.wait()