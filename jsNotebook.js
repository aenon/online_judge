
const DefaultMap = (defaultValue = undefined) => {
    const map = new Map()
    const set = (key, value) => {
        map.set(key, value)
    }
    const get = key => {
        if (map.get('a')) {
            return map.get('a')
        }
        return defaultValue
    }
    return {set, get}
}

const myStack = []
myStack.push(1)
myStack.pop()

const myQ = []
myQ.push(1)
myQ.push(2)
myQ.shift()
myQ

const createSLL = () => {
    let head = null
    
    const getHead = () => head
    
    const push = value => {
        let node = {value, next: null}
        if (!head) {
            head = node
        }
        else {
            let current = head
            while (current.next) {
                current = current.next
            }
            current.next = node
        }
    }
    return {getHead, push}
}

var sll = createSLL()

sll.push(3);
sll.push(4);
sll.push(5);

sll.getHead()

var createDLL = () => {
    let head = null
    const getHead = () => head
    const push = value => {
        let current = head
        let previous = head
        if (!head) {
            head = {value, previous: null, next: null}
        }
        else {
            while (current && current.next) {
                previous = current
                current = current.next
            }
            current.next = {value, previous: current, next: null}
        }
    }
    return {getHead, push}
}

var dll = createDLL()
dll.push(2)
dll.push(3)
dll.push(4)
dll.push(5)

dll.getHead().next.previous

const adjacencyMatrix = DefaultMap(DefaultMap(false))

for (valuePair of [
    [0, 1],
    [0, 5],
    [0, 4],
    [1, 3],
    [1, 4],
    [2, 1],
    [3, 2],
    [3, 4]
]){
    adjacencyMatrix.get(valuePair[0]).set(valuePair[1], true)
}

adjacencyMatrix.get(1).get(1)

adjacencyMatrix.get(1).set(1, 50)

adjacencyMatrix.get(1).get(1)

adjacencyMatrix.get(1).get(3)

var sayHi = name => console.log(`Hello, ${name}!`)
sayHi('Harry')


var twoSum = (nums, target) => {
    for (const i of [...Array(nums.length).keys()]) {
        if (nums.includes(target - nums[i])) {
            const j = +Object.keys(nums).find(key => nums[key] == target - nums[i] && key != i)
            if (j) {
                return [i, j]
            }
        }
    }
    return "not found"
}

function ListNode(val) {
    this.val = val;
    this.next = null;
}

function appendAtEnd(Node, val) {
    if (!Node.next) {
        Node.next = ListNode(value)
    }
    else {
        appendAtEnd(Node.next, val)
    }
}

var list1 = ListNode(2)

list1

function foo() {
    let a = 2
    function bar() {
        console.log(a)
    }
    return bar
}

var baz = foo()

baz()

var foo = () => {
    let  a = 2
    var bar = () => console.log(a)
    return {bar}
}

var baz = foo()

baz.bar()
