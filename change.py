bigData = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
quantity = ["圆", "拾", "佰", "仟", "万"]


def isNum():
    num = input("请输入需要转换的数字：")
    if num.isdecimal() and len(num) < 13:
        element = num.lstrip("0")
        reult = bigWord(element)
        print(reult)
    else:
        print("输入的内容不符合规范")


def bigWord(element):
    result = ""
    list = element.split(".")
    if len(list) == 1:
        nums = list[0]
        for i in range(0, len(nums)):
            if int(nums[i]) != 0:
                result += bigData[int(nums[i])] + quantity[len(nums)-i-1]
            else:
                if result[-1] != "零":
                    result += "零"
        return result + "整"


if __name__ == "__main__":
    isNum()
