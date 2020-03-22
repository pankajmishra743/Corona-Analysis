function barGraph(dates,sData,aData) {
	$('#barChart').remove(); // this is my <canvas> element
  $('#ChartContainer').append('<canvas id="barChart" width="1000" height="450"></canvas>');
var densityCanvas = document.getElementById("barChart");

Chart.defaults.global.defaultFontFamily = "Lato";
Chart.defaults.global.defaultFontSize = 18;

var stateData = {
  label: 'Selection Based Count',
  data: sData,
  backgroundColor: 'rgba(25, 108, 225, 1)',
  borderWidth: 0,
  yAxisID: "y-axis-home"
};

var allData = {
  label: 'All India Count',
  data: aData,
  backgroundColor: 'rgba(225, 125, 25, 1)',
  borderWidth: 0,
  //yAxisID: "y-axis-away"
};

var chartData = {
  labels: dates,
  datasets: [stateData,allData]
};

var chartOptions = {
  scales: {
    xAxes: [{
      barPercentage: 1,
      categoryPercentage: 1.0
    }],
    yAxes: [{
      id: "y-axis-home",
	  ticks:{
              beginAtZero:true,
			  stepSize: 50
	  }
    }
	    //, {
      //id: "y-axis-away",
	//  ticks:{
          ///    beginAtZero:true
	  //}
    //}
	   ]
  }
};

var barChart = new Chart(densityCanvas, {
  type: 'bar',
  data: chartData,
  options: chartOptions
});
}
