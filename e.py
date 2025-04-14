import sys
import itertools


class Idfentifier:
    def __init__(self, codes):
        self.codes = codes
        self.options = [
            getattr(self, method) for method in dir(self) if method.startswith("option")
        ]


class Card_1(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[0] == 1)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[0] != 1)


class Card_2(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[0] < 3)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[0] == 3)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[0] > 3)


class Card_3(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[1] < 3)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[1] == 3)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[1] > 3)


class Card_4(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[1] < 4)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[1] == 4)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[1] > 4)


class Card_5(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[0] % 2)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[0] % 2 == 0)


class Card_6(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[1] % 2 == 1)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[1] % 2 == 0)


class Card_7(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[2] % 2)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[2] % 2 == 0)


class Card_8(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if 1 not in code)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code.count(1) == 1)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code.count(1) == 2)

    def optionD(self):
        self.newcodes = tuple(code for code in self.codes if code.count(1) == 3)


class Card_9(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if 3 not in code)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code.count(3) == 1)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code.count(3) == 2)

    def optionD(self):
        self.newcodes = tuple(code for code in self.codes if code.count(3) == 3)


class Card_10(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if 4 not in code)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code.count(4) == 1)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code.count(4) == 2)

    def optionD(self):
        self.newcodes = tuple(code for code in self.codes if code.count(4) == 3)


class Card_11(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[0] < code[1])

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[0] == code[1])

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[0] > code[1])


class Card_12(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[0] < code[2])

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[0] == code[2])

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[0] > code[2])


class Card_13(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[1] < code[2])

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[1] == code[2])

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[1] > code[2])


class Card_14(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(
            code for code in self.codes if code[0] < code[1] and code[0] < code[2]
        )

    def optionB(self):
        self.newcodes = tuple(
            code for code in self.codes if code[1] < code[0] and code[1] < code[2]
        )

    def optionC(self):
        self.newcodes = tuple(
            code for code in self.codes if code[2] < code[0] and code[2] < code[1]
        )


class Card_15(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(
            code for code in self.codes if code[0] > code[1] and code[0] > code[2]
        )

    def optionB(self):
        self.newcodes = tuple(
            code for code in self.codes if code[1] > code[0] and code[1] > code[2]
        )

    def optionC(self):
        self.newcodes = tuple(
            code for code in self.codes if code[2] > code[0] and code[2] > code[1]
        )


class Card_16(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(
            code for code in self.codes if (code[0] % 2 + code[1] % 2 + code[2] % 2) < 2
        )

    def optionB(self):
        self.newcodes = tuple(
            code
            for code in self.codes
            if (code[0] % 2 + code[1] % 2 + code[2] % 2) >= 2
        )


class Card_17(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(
            code for code in self.codes if code[0] % 2 + code[1] % 2 + code[2] % 2 == 3
        )

    def optionB(self):
        self.newcodes = tuple(
            code for code in self.codes if code[0] % 2 + code[1] % 2 + code[2] % 2 == 2
        )

    def optionD(self):
        self.newcodes = tuple(
            code for code in self.codes if code[0] % 2 + code[1] % 2 + code[2] % 2 == 1
        )

    def optionC(self):
        self.newcodes = tuple(
            code for code in self.codes if code[0] % 2 + code[1] % 2 + code[2] % 2 == 0
        )


class Card_18(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(
            code for code in self.codes if (code[0] + code[1] + code[2]) % 2 == 0
        )

    def optionB(self):
        self.newcodes = tuple(
            code for code in self.codes if (code[0] + code[1] + code[2]) % 2 == 1
        )


class Card_19(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[0] + code[1] < 6)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[0] + code[1] == 6)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[0] + code[1] > 6)


class Card_20(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if len(set(code)) == 1)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if len(set(code)) == 2)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if len(set(code)) == 3)


class Card_21(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if len(set(code)) == 2)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if len(set(code)) != 2)


class Card_22(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(
            code for code in self.codes if code[0] < code[1] < code[2]
        )

    def optionB(self):
        self.newcodes = tuple(
            code for code in self.codes if code[0] > code[1] > code[2]
        )

    def optionC(self):
        self.newcodes = tuple(
            code
            for code in self.codes
            if not (code[0] < code[1] < code[2] or code[0] > code[1] > code[2])
        )


class Card_23(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(
            code for code in self.codes if code[0] + code[1] + code[2] < 6
        )

    def optionB(self):
        self.newcodes = tuple(
            code for code in self.codes if code[0] + code[1] + code[2] == 6
        )

    def optionC(self):
        self.newcodes = tuple(
            code for code in self.codes if code[0] + code[1] + code[2] > 6
        )


class Card_24(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(
            code for code in self.codes if code[0] + 2 == code[1] + 1 == code[2]
        )

    def optionB(self):
        self.newcodes = tuple(
            code
            for code in self.codes
            if not (code[0] + 2 == code[1] + 1 == code[2])
            and (code[0] + 1 == code[1] or code[1] + 1 == code[2])
        )

    def optionC(self):
        self.newcodes = tuple(
            code
            for code in self.codes
            if not (code[0] + 2 == code[1] + 1 == code[2])
            and not (code[0] + 1 == code[1] or code[1] + 1 == code[2])
        )


class Card_25(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(
            code
            for code in self.codes
            if not (
                code[0] + 2 == code[1] + 1 == code[2]
                or code[0] - 2 == code[1] - 1 == code[2]
            )
            and not (
                code[0] + 1 == code[1]
                or code[1] + 1 == code[2]
                or code[0] - 1 == code[1]
                or code[1] - 1 == code[2]
            )
        )

    def optionB(self):
        self.newcodes = tuple(
            code
            for code in self.codes
            if not (
                code[0] + 2 == code[1] + 1 == code[2]
                or code[0] - 2 == code[1] - 1 == code[2]
            )
            and (
                code[0] + 1 == code[1]
                or code[1] + 1 == code[2]
                or code[0] - 1 == code[1]
                or code[1] - 1 == code[2]
            )
        )

    def optionC(self):
        self.newcodes = tuple(
            code
            for code in self.codes
            if code[0] + 2 == code[1] + 1 == code[2]
            or code[0] - 2 == code[1] - 1 == code[2]
        )


class Card_26(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[0] < 3)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[1] < 3)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[2] < 3)


class Card_27(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[0] < 4)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[1] < 4)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[2] < 4)


class Card_28(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[0] == 1)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[1] == 1)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[2] == 1)


class Card_29(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[0] == 3)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[1] == 3)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[2] == 3)


class Card_30(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[0] == 4)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[1] == 4)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[2] == 4)


class Card_31(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[0] > 1)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[1] > 1)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[2] > 1)


class Card_32(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[0] > 3)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[1] > 3)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[2] > 3)


class Card_33(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[0] % 2 == 0)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[0] % 2 == 1)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[1] % 2 == 0)

    def optionD(self):
        self.newcodes = tuple(code for code in self.codes if code[1] % 2 == 1)

    def optionE(self):
        self.newcodes = tuple(code for code in self.codes if code[2] % 2 == 0)

    def optionF(self):
        self.newcodes = tuple(code for code in self.codes if code[2] % 2 == 1)


class Card_34(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(
            code for code in self.codes if code[0] <= code[1] and code[0] <= code[2]
        )

    def optionB(self):
        self.newcodes = tuple(
            code for code in self.codes if code[1] <= code[0] and code[1] <= code[2]
        )

    def optionC(self):
        self.newcodes = tuple(
            code for code in self.codes if code[2] <= code[0] and code[2] <= code[1]
        )


class Card_35(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(
            code for code in self.codes if code[0] >= code[1] and code[0] >= code[2]
        )

    def optionB(self):
        self.newcodes = tuple(
            code for code in self.codes if code[1] >= code[0] and code[1] >= code[2]
        )

    def optionC(self):
        self.newcodes = tuple(
            code for code in self.codes if code[2] >= code[0] and code[2] >= code[1]
        )


class Card_36(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(
            code for code in self.codes if (code[0] + code[1] + code[2]) % 3 == 0
        )

    def optionB(self):
        self.newcodes = tuple(
            code for code in self.codes if (code[0] + code[1] + code[2]) % 4 == 0
        )

    def optionC(self):
        self.newcodes = tuple(
            code for code in self.codes if (code[0] + code[1] + code[2]) % 5 == 0
        )


class Card_37(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[0] + code[1] == 4)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[0] + code[2] == 4)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[1] + code[2] == 4)


class Card_38(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[0] + code[1] == 6)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[0] + code[2] == 6)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[1] + code[2] == 6)


class Card_39(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[0] == 1)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[0] > 1)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[1] == 1)

    def optionD(self):
        self.newcodes = tuple(code for code in self.codes if code[1] > 1)

    def optionE(self):
        self.newcodes = tuple(code for code in self.codes if code[2] == 1)

    def optionF(self):
        self.newcodes = tuple(code for code in self.codes if code[2] > 1)


class Card_40(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[0] < 3)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[0] == 3)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[0] > 3)

    def optionD(self):
        self.newcodes = tuple(code for code in self.codes if code[1] < 3)

    def optionE(self):
        self.newcodes = tuple(code for code in self.codes if code[1] == 3)

    def optionF(self):
        self.newcodes = tuple(code for code in self.codes if code[1] > 3)

    def optionG(self):
        self.newcodes = tuple(code for code in self.codes if code[2] < 3)

    def optionH(self):
        self.newcodes = tuple(code for code in self.codes if code[2] == 3)

    def optionI(self):
        self.newcodes = tuple(code for code in self.codes if code[2] > 3)


class Card_41(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[0] < 4)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[0] == 4)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[0] > 4)

    def optionD(self):
        self.newcodes = tuple(code for code in self.codes if code[1] < 4)

    def optionE(self):
        self.newcodes = tuple(code for code in self.codes if code[1] == 4)

    def optionF(self):
        self.newcodes = tuple(code for code in self.codes if code[1] > 4)

    def optionG(self):
        self.newcodes = tuple(code for code in self.codes if code[2] < 4)

    def optionH(self):
        self.newcodes = tuple(code for code in self.codes if code[2] == 4)

    def optionI(self):
        self.newcodes = tuple(code for code in self.codes if code[2] > 4)


class Card_42(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(
            code for code in self.codes if code[0] < code[1] and code[0] < code[2]
        )

    def optionB(self):
        self.newcodes = tuple(
            code for code in self.codes if code[0] > code[1] and code[0] > code[2]
        )

    def optionC(self):
        self.newcodes = tuple(
            code for code in self.codes if code[1] < code[0] and code[1] < code[2]
        )

    def optionD(self):
        self.newcodes = tuple(
            code for code in self.codes if code[1] > code[0] and code[1] > code[2]
        )

    def optionE(self):
        self.newcodes = tuple(
            code for code in self.codes if code[2] < code[0] and code[2] < code[1]
        )

    def optionF(self):
        self.newcodes = tuple(
            code for code in self.codes if code[2] > code[0] and code[2] > code[1]
        )


class Card_43(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[0] < code[1])

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[0] < code[2])

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[0] == code[1])

    def optionD(self):
        self.newcodes = tuple(code for code in self.codes if code[0] == code[2])

    def optionE(self):
        self.newcodes = tuple(code for code in self.codes if code[0] > code[1])

    def optionF(self):
        self.newcodes = tuple(code for code in self.codes if code[0] > code[2])


class Card_44(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[1] < code[0])

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[1] < code[2])

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[1] == code[0])

    def optionD(self):
        self.newcodes = tuple(code for code in self.codes if code[1] == code[2])

    def optionE(self):
        self.newcodes = tuple(code for code in self.codes if code[1] > code[0])

    def optionF(self):
        self.newcodes = tuple(code for code in self.codes if code[1] > code[2])


class Card_45(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code.count(1) == 0)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code.count(3) == 0)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code.count(1) == 1)

    def optionD(self):
        self.newcodes = tuple(code for code in self.codes if code.count(3) == 1)

    def optionE(self):
        self.newcodes = tuple(code for code in self.codes if code.count(1) == 2)

    def optionF(self):
        self.newcodes = tuple(code for code in self.codes if code.count(3) == 2)


class Card_46(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code.count(3) == 0)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code.count(4) == 0)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code.count(3) == 1)

    def optionD(self):
        self.newcodes = tuple(code for code in self.codes if code.count(4) == 1)

    def optionE(self):
        self.newcodes = tuple(code for code in self.codes if code.count(3) == 2)

    def optionF(self):
        self.newcodes = tuple(code for code in self.codes if code.count(4) == 2)


class Card_47(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code.count(1) == 0)

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code.count(4) == 0)

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code.count(1) == 1)

    def optionD(self):
        self.newcodes = tuple(code for code in self.codes if code.count(4) == 1)

    def optionE(self):
        self.newcodes = tuple(code for code in self.codes if code.count(1) == 2)

    def optionF(self):
        self.newcodes = tuple(code for code in self.codes if code.count(4) == 2)


class Card_48(Idfentifier):
    def __init__(self, codes):
        super().__init__(codes)

    def optionA(self):
        self.newcodes = tuple(code for code in self.codes if code[0] < code[1])

    def optionB(self):
        self.newcodes = tuple(code for code in self.codes if code[0] == code[1])

    def optionC(self):
        self.newcodes = tuple(code for code in self.codes if code[0] > code[1])

    def optionD(self):
        self.newcodes = tuple(code for code in self.codes if code[0] < code[2])

    def optionE(self):
        self.newcodes = tuple(code for code in self.codes if code[0] == code[2])

    def optionF(self):
        self.newcodes = tuple(code for code in self.codes if code[0] > code[2])

    def optionG(self):
        self.newcodes = tuple(code for code in self.codes if code[1] < code[2])

    def optionH(self):
        self.newcodes = tuple(code for code in self.codes if code[1] == code[2])

    def optionI(self):
        self.newcodes = tuple(code for code in self.codes if code[1] > code[2])


def is_valid(code, used, codes, n):
    if len(code) != 1:
        return False
    for method_combo in itertools.combinations(used, n - 1):
        current_codes = codes

        for m in method_combo:
            card_cls = m.__self__.__class__
            method_name = m.__name__

            card_instance = card_cls(current_codes)
            getattr(card_instance, method_name)()

            current_codes = card_instance.newcodes

        if len(current_codes) == 1:
            return False

    return True


def main():
    cards = []

    for argv in sys.argv[1:]:
        if argv.isdigit() and 1 <= int(argv) <= 48:
            card_class = globals()["Card_" + argv]
            cards.append(card_class)
        else:
            print(
                f"Usage: {sys.argv[0]} card1 ... cardN.",
                file=sys.stderr,
            )
            return

    codes = list(itertools.product(range(1, 6), repeat=3))
    card_instances = [cls(codes) for cls in cards]
    sequences = itertools.combinations(card_instances, len(cards))

    for card_seq in sequences:
        option_lists = [card.options for card in card_seq]
        for method_seq in itertools.product(*option_lists):
            used = []
            current_codes = codes

            for m in method_seq:
                card_instance = m.__self__.__class__(current_codes)

                method_name = m.__name__
                method = getattr(card_instance, method_name)
                used.append(method)
                method()

                current_codes = card_instance.newcodes

            if is_valid(current_codes, used, codes, len(cards)):
                print(
                    "Solution found",
                    current_codes[0],
                    "with",
                    " ".join(
                        f"{m.__self__.__class__.__name__}:{m.__name__}"
                        for m in method_seq
                    ),
                )


if __name__ == "__main__":
    main()
