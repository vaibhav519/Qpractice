function rangeOfNumbers(startNum, endNum) {
    if (startNum > endNum){
      return []
    }
    else{
      let array = rangeOfNumbers(startNum, endNum - 1)
      array.push(endNum)
      return array
    }
  };

rangeOfNumbers(1, 5)