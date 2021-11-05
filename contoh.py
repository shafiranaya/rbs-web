from experta import *


class Loads(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="load")

    @Rule(Fact(action='load'), NOT(Fact(fulltime=W())))
    def ask_id(self):
        self.declare(
            Fact(fulltime=input("Is the applicant a full time employee? ")))

    # Rule 1:whether is full time
    # full time
    @Rule(Fact(action='load'), (Fact(fulltime='yes')))
    def ask_year_3(self):
        self.declare(
            Fact(Three_year=input("Have they been with the bank over 3 years? ")))
    # not full time or not sure
    @Rule(Fact(action='load'), OR(Fact(fulltime='not sure'), Fact(fulltime='no')))
    def ask_year_5(self):
        self.declare(
            Fact(Five_year=input("Have they been with the bank over 5 years? ")))

    # Rule 2 accept
    @Rule(Fact(action='load'), AND(Fact(fulltime='yes'), Fact(Three_year='yes')))
    def accept_1(self):
        print("Grant Load")

    # Rule 3: full time but not sure or not work over 3 year
    @Rule(Fact(action='load'), AND(Fact(fulltime='yes'), OR(Fact(Three_year='no'), Fact(Three_year='not sure'))))
    def ask_pre_load(self):
        self.declare(
            Fact(pre_load=input(" Have they had a previous loan? ")))
    # Rule 3:not full time or not sure but work over 5 year
    @Rule(Fact(action='load'), AND(OR(Fact(fulltime='not sure'), (Fact(fulltime='no'))), Fact(Five_year='yes')))
    def ask_pre_load(self):
        self.declare(
            Fact(pre_load=input(" Have they had a previous loan? ")))

    # Rule 3 reject: not or not sure fulltime and not or not sure  work over 5 year
    @Rule(Fact(action='load'), AND(OR(Fact(fulltime='not sure')), (Fact(fulltime='no'))), OR(Fact(Five_year='not sure'), Fact(Five_year='no')))
    def reject_1(self):
        print("Reject load")

    # Rule 4: Whether has previous load
    @Rule(Fact(action='load'), Fact(pre_load='yes'))
    def ask_paid_on_time(self):
        self.declare(
            Fact(on_time=input("And was that load repaid on time? ")))
    # Rule 4 reject: not had previous load
    @Rule(Fact(action='load'), OR(Fact(pre_load='not sure'), Fact(pre_load='no')))
    def reject_2(self):
        print("Reject load")
    # Whether repaid on time
    # Accept: Repaid on time
    @Rule(Fact(action='load'), Fact(on_time='yes'))
    def accept_2(self):
        print("Accept load")
    # Reject: not or not sure repaid on time
    @Rule(Fact(action='load'), OR(Fact(on_time='not sure'), Fact(on_time='no')))
    def reject_3(self):
        print("Reject load")


engine = Loads()
engine.reset()
engine.run()