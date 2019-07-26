'''
穷举法

四人分🐟：
        A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
        第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
        B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
        然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼

分析：
        A醒来的时候有X5条🐟，则
        X4=(X5-1) // 5 * 4
        X3=(X4-1) // 5 * 4
        X2=(X3-1) // 5 * 4
        X1=(X2-1) // 5 * 4
        且必须满足（X5-1）～（X1-1）都能整除5
'''
fish = 6
while True:
        now_fish = fish
        enough_flag = True
        for _ in range(5):
                if not (now_fish-1)%5:
                        now_fish = (now_fish-1) // 5 * 4
                else:
                        enough_flag = False
                        break;

        if enough_flag:
                print(fish)
                break;
        fish += 5
