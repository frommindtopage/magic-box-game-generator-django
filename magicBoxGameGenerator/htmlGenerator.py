from random import choice
def totalMatch(l1,l2):
    return sum([l1[x]==l2[x] for x in range(len(l1))])
def matrixGenerator(height,width):
    matrix= [[x//width,x%width]  for x in range(height*width)]
    match=matrix.copy()
    def directionAvailable():
        available=[]
        if(matrix[-1][0]!=0):
            available+=[[-1,0]]
        if(matrix[-1][0]!=height-1):
            available+=[[+1,0]]
        if(matrix[-1][-1]!=0):
            available+=[[0,-1]]
        if(matrix[-1][-1]!=width-1):
            available+=[[0,+1]]
        return choice(available)
    def positionChange():
        direction=directionAvailable()
        newPosition= [matrix[-1][0]+direction[0],matrix[-1][1]+direction[1]]
        exchangeIndex=matrix.index(newPosition)
        matrix[-1],matrix[exchangeIndex]=matrix[exchangeIndex],matrix[-1]
        return matrix
    for x in range(height*width*1000):
        matrix=positionChange()
    while(totalMatch(matrix,match)!=0):
        matrix=positionChange()
    return matrix,match
def htmlGenerator(height,width):
    timeLimit = height*width*20
    s=""
    s+='''<!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Magic'''+str(height)+'X'+str(width)+'''</title>
        <link rel="stylesheet" href="assets/css/style.css">
        <!-------------------------------------------------------------------------------->
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Finger+Paint&display=swap" rel="stylesheet">
            <style>
        #percantage {
            text-align: right;
        }
        #timer {
            text-align:left;
        }
        table {
            user-select: none;
            border-collapse: collapse;
        }
        .box {
            background-color: black;
            color: rgba(255, 0, 0, 0.823);
            font-size: 50px;
            font-family: 'Finger Paint', cursive;
            text-align: center;
            width: 100px;
            height: 100px;
            background-size: 100px 100px;
            margin: 0px;
        }

        h6 {
            color: red;
            margin-top: 5px;
        }
        #instruction,
        h6 {
            margin-bottom: 5px;
        }
        #info {
            width: '''+str(103.33*width)+'''px;
            display: flex;
            flex-direction: row;
            justify-content: space-between;
        }
    </style>
    </head>
    '''
    s+="""<body>
    <div id="instruction"><b>you can move the block by mouse or arrow keys</div>
    <div id="instruction" style="color:red"><b>you can't able to take number of columns and rows less than 3 and more than 10</b></div>
    <h6 id="info">
        <div id="timer">Time left """+"0"*(2-len(str(timeLimit//60)))+str(timeLimit//60)+" : "+"0"*(2-len(str(timeLimit%60)))+str(timeLimit%60)+"""</div>
        <div id="percantage">percantage completed 0%</div>
    </h6>
    <table border="1">"""
    n=0
    problem,match=matrixGenerator(height,width)
    for x in range(height):
        s+="""<tr>
        """
        for y in range(width):
            id=problem.index([n//width,n%width])
            s+="""<td class="box" id="box-"""+"0"*(2-len(str(id)))+str(id)+""""></td>
            """
            n+=1
        s+="""
        </tr>
        """
    s+="""    </table>
        <div id="score-board">

        </div>"""
    s+="""<script>
        //position of each block
        let position = """+str(problem)+"""
        let match = """+str(match)+"""
        let boxList = """+str(["box-"+"0"*(2-len(str(x)))+str(x) for x in range(height*width)])+"""
        let arrowEffect = false   //If arrowEffect=true the block moves in the direction of the arrow button clicked but if arrowEffect=false the block moves in the opposite direction of the arrow button clicked
        let height = """+str(height)+"""
        let width = """+str(width)+"""
        let minOpacity = .1
        let step = 0
        let status = "process"
        let timePassed = 0
        let leftTime = """+str(timeLimit)+"""
        """
    s+="""function getElement(identity, By = '.', update = false, updateData = null, updateType = "text") {
            if (By === '.') {
                element = document.getElementById(identity)
                if (update) {
                    if (updateType == "text") {
                        element.innerText = updateData
                    } else {
                        element.innerHTML = updateData
                    }
                } else {
                    return element
                }
            }
            else {
                element = document.getElementsByClassName(identity)
                return element
            }
        }


        //timeConverter
        function timeConverter(Time) {
            let minute = String(Math.floor(Time / 60))
            let second = String(Time % 60)
            if (minute.length == 1) {
                minute = "0" + minute
            }
            if (second.length == 1) {
                second = "0" + second
            }
            return [minute, second]
        }
        //Compare two list
        function compareList(l1, l2) {
            return JSON.stringify(l1) === JSON.stringify(l2)
        }
        //result
        function scoreBoard() {
            let result = ""
            result += "Result :-" + status + "<br>"
            timeConverter(timePassed)
            result += "Time Taken :-" + timeConverter(timePassed)[0] + ' : ' + timeConverter(timePassed)[1] + "<br>"
            getElement('score-board', '.', true, result, 'html')
        }

        //detecting arrow key presses
        document.addEventListener('keydown', function (e) {
            if (arrowEffect) {
                dirInfor = { 38: { X: -1, Y: 0 }, 40: { X: +1, Y: 0 }, 37: { X: 0, Y: -1 }, 39: { X: 0, Y: +1 } }
                limit = { 38: 0, 40: height - 1, 37: 0, 39: width - 1 }
            }
            else {
                dirInfor = { 38: { X: 1, Y: 0 }, 40: { X: -1, Y: 0 }, 37: { X: 0, Y: 1 }, 39: { X: 0, Y: -1 } }
                limit = { 38: height - 1, 40: 0, 37: width - 1, 39: 0 }
            }
            if (e.keyCode in dirInfor) {
                if (position["""+str(height*width-1)+"""][1 - Math.abs(dirInfor[e.keyCode].X)] !== limit[e.keyCode]) {
                    getElement(boxList[find([position["""+str(height*width-1)+"""][0] + dirInfor[e.keyCode].X, position["""+str(height*width-1)+"""][1] + dirInfor[e.keyCode].Y])]).click()
                }
            }
        })"""
    s+="""//background
        function background() {
            let i = 0
            for (block of getElement('box', '#')) {
                if (block.id.slice(4) !== '"""+'0'*(2-len(str(height*width-1)))+str(height*width-1)+"""') {
                    block.innerText = block.id.slice(4)
                    if (compareList(position[find(block.id, boxList)], match[find(block.id, boxList)])) {
                        block.style.color = "green";
                        i++
                    }
                    else {
                        block.style.color = "red"
                    }
                }
                else {
                    block.innerText = ""
                }
            }
            if (compareList(position["""+str(height*width-1)+"""], ["""+str(height-1)+""", """+str(width-1)+"""])) {
                i = i + 1
            }
            getElement('percantage', '.', true, "Completed   " + ((i / """+str(height*width)+""") * 100).toFixed(2) + '%')
            getElement('percantage').style.opacity = minOpacity + (i / """+str(height*width)+""") / (1 - minOpacity)
        }
        background()


        ////////////////////timer
        let timer = setInterval(() => {
            //let minutePassed = String(Math.floor(timePassed / 60))
            getElement("timer", ".", true, "Time left " + timeConverter(leftTime)[0] + " : " + timeConverter(leftTime)[1])
            if (leftTime === 0) {
                status = "Fail"
                scoreBoard()
                setTimeout(() => {
                    alert("Time out");
                }, 0);
                getElement('timer').remove()
                clearInterval(timer)
            }
            if (step !== 0 & status==="process") {
                leftTime--
                timePassed++
            }
        }, 1000);

        //Find
        function find(d, list = position) {
            for (ab = 0; ab <= """+str(height*width-1)+"""; ab++) {
                if (compareList(list[ab], d)) {
                    return ab
                }
            }
        }

        //reverse
        function reverse(content, condition) {
            if (condition) {
                content.reverse()
            }
            return content
        }

        //give between number list function
        function btw(element, y) {
            x1 = position[parseInt(element.id.slice(4))][y]
            y1 = position[parseInt(element.id.slice(4))][1 - y]
            let li = []
            for (x = Math.min(x1, position["""+str(height*width-1)+"""][y]); x <= Math.max(x1, position["""+str(height*width-1)+"""][y]); x++) {
                li[li.length] = getElement(boxList[find(reverse([x, y1], y == 1))])
            }
            return reverse(li, x1 < position["""+str(height*width-1)+"""][y]).slice(1)
        }

        //inline or not
        function inline(element) {
            let l = position[parseInt(element.id.slice(4))]
            if (l[0] === position["""+str(height*width-1)+"""][0] & l[1] !== position["""+str(height*width-1)+"""][1]) {
                return 1
            } else if (l[1] === position["""+str(height*width-1)+"""][1] & l[0] !== position["""+str(height*width-1)+"""][0]) {
                return 0
            }
            else {
                return false
            }
        }"""
    s+="""    //adding EventListener 
            for (block of getElement('box', "#")) {
                block.addEventListener('click', click)
                function click(e) {
                    if (inline(e.target) !== false & status === "process") {
                        for (element of btw(e.target, inline(e.target))) {
                            document.getElementById(boxList[boxList.length-1]).id = element.id
                            let temB = position["""+str(height*width-1)+"""]
                            position["""+str(height*width-1)+"""] = position[find(element.id, boxList)]
                            position[find(element.id, boxList)] = temB
                            element.id = boxList[boxList.length-1]
                        }
                        step++
                        background()
                        if (compareList(position, match)) {
                            setTimeout(() => {
                                alert("You win ");
                            }, 0);
                            status = "pass"
                            scoreBoard()
                        }
                    }
                }
            }</script>
            </body>
            </html>"""
    return s
