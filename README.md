## 有想要研究程式的可以參考我爬出來的最新小恐龍程式碼(4000多行)
### 修改就是用 F12 的 console 視窗調整內部程式碼，神奇的是 JS 的物件都是 public 的所以可以輕鬆在外部修改
<br>
<br>
<br>
<br>

# 科普小恐龍操作流程
## 前置
1. 開啟小恐龍，在 google 搜尋欄打上
    ```terminal
    chrome://dino
    ```
3. 按 `F12` 打開除錯頁面
4. 在 console 輸入
    ```terminal
    //取得小恐龍物件
    var dino = Runner.getInstance()
    //取得小恐龍物件的內物件
    var TREX = dino.tRex
    //取得小恐龍設定
    var Dconfig = dino.getConfig()
    ```
5. 先試跑一次，game over 在修改數值
## 作弊碼
```terminal
//調整速度
Dconfig.speed = 1000

//調整重力，影響跳躍
TREX.config.gravity = 0.2

//無敵，無法 gameover
dino.gameOver = function(){}

//取消無敵，回復原始設定
dino.gameOver = Runner.prototype.gameOver

//調整起跳速度，值越小，跳越高
TREX.config.initialJumpVelocity = -200

//遊戲加速度
Dconfig.acceleration = 10

//掉落速度，值越大，掉落越快
TREX.config.dropVelocity = 5

//障礙物出現間隔，越小障礙物愈密集
dino.horizon.gapCoefficient = -2

//把最高分紀錄歸零
dino.saveHighScore(0,false)
```
