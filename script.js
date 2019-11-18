function scrollVertical(element, quantity) {
  element.scrollTop += quantity;
}
function scrollHorizontal(element, quantity) {
  element.scrollLeft += quantity;
}
function createArray(row, cols) {
  var x = new Array(row);

  for (var i = 0; i < x.length; i++) {
    x[i] = new Array(cols);
  }
  return x;

}
function download(data, filename, type) {
    var file = new Blob([data], {type: type});
    if (window.navigator.msSaveOrOpenBlob) // IE10+
        window.navigator.msSaveOrOpenBlob(file, filename);
    else { // Others
        var a = document.createElement("a"),
                url = URL.createObjectURL(file);
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        setTimeout(function() {
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
        }, 0);
    }
}
function getTiming(done) {
  var pixel = document.getElementById("enlargedDiv");

  var hrt_st = performance.now();

  pixel.classList.add("timing");

  requestAnimationFrame(function(startTime) {
    var hrt_end = performance.now();
    pixel.classList.remove("timing");
    requestAnimationFrame(function(endTime) {
      done(hrt_end - hrt_st, document.getElementById('imageDiv').scrollTop, document.getElementById('imageDiv').scrollLeft)
    });
  });
}
