(function ($) {
    "use strict";
    // var loadData = function () {
    //     $.ajax({
    //         type: "GET",
    //         url: "/data", // Assuming your server provides a '/data' endpoint
    //         dataType: "json",
    //         success: function (data) {
    //             // Process the data and use it in your charts
    //             console.log('Data loaded:', data);

    //             // Now you can use the 'data' variable to update your charts or perform other actions
    //             updateCharts(data);
    //         },
    //         error: function (error) {
    //             console.error('Error loading data:', error);
    //         }
    //     });
    // };

    // // Function to update charts with the loaded data
    // var updateCharts = function (data) {
    //     // Use the 'data' variable to update your charts
    //     // For example, assuming the structure of 'data' is suitable for your charts
    //     // Update the 'myChart1', 'myChart2', etc., as per your chart identifiers

    //     // Update Worldwide Sales Chart
    //     myChart1.data.labels = data.labels;
    //     myChart1.data.datasets[0].data = data.usaData;
    //     myChart1.data.datasets[1].data = data.ukData;
    //     myChart1.data.datasets[2].data = data.auData;
    //     myChart1.update();

    //     // Update Salse & Revenue Chart
    //     myChart2.data.labels = data.labels;
    //     myChart2.data.datasets[0].data = data.salseData;
    //     myChart2.data.datasets[1].data = data.revenueData;
    //     myChart2.update();

    //     // Update Single Line Chart
    //     myChart3.data.labels = data.lineChartLabels;
    //     myChart3.data.datasets[0].data = data.lineChartData;
    //     myChart3.update();

    //     // Update Single Bar Chart
    //     myChart4.data.labels = data.barChartLabels;
    //     myChart4.data.datasets[0].data = data.barChartData;
    //     myChart4.update();

    //     // Update Pie Chart
    //     myChart5.data.labels = data.pieChartLabels;
    //     myChart5.data.datasets[0].data = data.pieChartData;
    //     myChart5.update();

    //     // Update Doughnut Chart
    //     myChart6.data.labels = data.doughnutChartLabels;
    //     myChart6.data.datasets[0].data = data.doughnutChartData;
    //     myChart6.update();
    // };

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Sidebar Toggler
    $('.sidebar-toggler').click(function () {
        $('.sidebar, .content').toggleClass("open");
        return false;
    });


    // Progress Bar
    $('.pg-bar').waypoint(function () {
        $('.progress .progress-bar').each(function () {
            $(this).css("width", $(this).attr("aria-valuenow") + '%');
        });
    }, {offset: '80%'});


    // Calender
    $('#calender').datetimepicker({
        inline: true,
        format: 'L'
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        items: 1,
        dots: true,
        loop: true,
        nav : false
    });

    $.ajax({
        url: '/per_course',
        type: 'GET',
        success: function(data) {
            var ctx1 = $("#pie-chart").get(0).getContext("2d");
            
            // Generate dynamic background colors based on the number of courses
            var backgroundColors = generateColors(data.course_names.length);
            
            var myChart1 = new Chart(ctx1, {
                type: "pie",
                data: {
                    labels: data.course_names,
                    datasets: [{
                        backgroundColor: backgroundColors,
                        data: data.num_students
                    }]
                },
                options: {
                    responsive: true
                }
            });
        }
    });
    
    // Function to generate dynamic background colors
    function generateColors(numColors) {
        var colors = [];
        var hueStep = 360 / numColors;
        for (var i = 0; i < numColors; i++) {
            // Generate hue
            var hue = (hueStep * i) % 360;
            // Generate saturation (between 40% and 100%)
            var saturation = Math.floor(Math.random() * 61) + 40;
            // Generate brightness (between 50% and 80%)
            var brightness = Math.floor(Math.random() * 31) + 50;
            // Convert HSB to RGB
            var rgbColor = hsbToRgb(hue, saturation, brightness);
            var rgbaColor = 'rgba(' + rgbColor.r + ',' + rgbColor.g + ',' + rgbColor.b + ',' + '0.7)';
            colors.push(rgbaColor);
        }
        return colors;
    }
    
    // Function to convert HSB to RGB
    function hsbToRgb(hue, saturation, brightness) {
        var chroma = (1 - Math.abs((2 * brightness / 100) - 1)) * (saturation / 100);
        var huePrime = hue / 60;
        var secondComponent = chroma * (1 - Math.abs((huePrime % 2) - 1));
        var red = 0, green = 0, blue = 0;
        if (huePrime >= 0 && huePrime < 1) {
            red = chroma;
            green = secondComponent;
        } else if (huePrime >= 1 && huePrime < 2) {
            red = secondComponent;
            green = chroma;
        } else if (huePrime >= 2 && huePrime < 3) {
            green = chroma;
            blue = secondComponent;
        } else if (huePrime >= 3 && huePrime < 4) {
            green = secondComponent;
            blue = chroma;
        } else if (huePrime >= 4 && huePrime < 5) {
            red = secondComponent;
            blue = chroma;
        } else if (huePrime >= 5 && huePrime < 6) {
            red = chroma;
            blue = secondComponent;
        }
        var lightness = brightness / 100 - chroma / 2;
        red += lightness;
        green += lightness;
        blue += lightness;
        return {
            r: Math.round(red * 255),
            g: Math.round(green * 255),
            b: Math.round(blue * 255)
        };
    }


    $.ajax({
        url: '/per_proctor',
        type: 'GET',
        success: function(data) {
            var ctx2 = $("#pie-chart-2").get(0).getContext("2d");
            
            // Generate dynamic background colors based on the number of proctors
            var backgroundColors = generateColors(data.supervisor_name.length);
            
            var myChart2 = new Chart(ctx2, {
                type: "pie",
                data: {
                    labels: data.supervisor_name,
                    datasets: [{
                        backgroundColor: backgroundColors,
                        data: data.num_student_per_supervisor
                    }]
                },
                options: {
                    responsive: true
                }
            });
        }
    });
    
    // Function to generate dynamic background colors
    function generateColors(numColors) {
        var colors = [];
        var hueStep = 360 / numColors;
        for (var i = 0; i < numColors; i++) {
            // Generate hue
            var hue = (hueStep * i) % 360;
            // Generate saturation (between 40% and 100%)
            var saturation = Math.floor(Math.random() * 61) + 40;
            // Generate brightness (between 50% and 80%)
            var brightness = Math.floor(Math.random() * 31) + 50;
            // Convert HSB to RGB
            var rgbColor = hsbToRgb(hue, saturation, brightness);
            var rgbaColor = 'rgba(' + rgbColor.r + ',' + rgbColor.g + ',' + rgbColor.b + ',' + '0.7)';
            colors.push(rgbaColor);
        }
        return colors;
    }
    
    // Function to convert HSB to RGB
    function hsbToRgb(hue, saturation, brightness) {
        var chroma = (1 - Math.abs((2 * brightness / 100) - 1)) * (saturation / 100);
        var huePrime = hue / 60;
        var secondComponent = chroma * (1 - Math.abs((huePrime % 2) - 1));
        var red = 0, green = 0, blue = 0;
        if (huePrime >= 0 && huePrime < 1) {
            red = chroma;
            green = secondComponent;
        } else if (huePrime >= 1 && huePrime < 2) {
            red = secondComponent;
            green = chroma;
        } else if (huePrime >= 2 && huePrime < 3) {
            green = chroma;
            blue = secondComponent;
        } else if (huePrime >= 3 && huePrime < 4) {
            green = secondComponent;
            blue = chroma;
        } else if (huePrime >= 4 && huePrime < 5) {
            red = secondComponent;
            blue = chroma;
        } else if (huePrime >= 5 && huePrime < 6) {
            red = chroma;
            blue = secondComponent;
        }
        var lightness = brightness / 100 - chroma / 2;
        red += lightness;
        green += lightness;
        blue += lightness;
        return {
            r: Math.round(red * 255),
            g: Math.round(green * 255),
            b: Math.round(blue * 255)
        };
    }
    
    $.ajax({
        url: '/violation_report',
        type: 'GET',
        success: function(data) {
            // Multiple Bar chart
            var ctx3 = $("#worldwide-sales").get(0).getContext("2d");
            var myChart3 = new Chart(ctx3, {
                type: "bar",
                data: {
                    labels: data.course_name,
                    datasets: [{
                            label: "Normal",
                            data: data.number_of_normal,
                            backgroundColor: "rgba(0, 156, 255, .7)"
                        },
                        {
                            label: "Abnormal",
                            data: data.number_of_abnormal,
                            backgroundColor: "rgba(255, 0, 0, .5)"
                        },
                    ]
                    },
                options: {
                    responsive: true
                }
            });
        }
    });

    $.ajax({
        url: '/vip_timeseries',
        type: 'GET',
        success: function(data) {
            // Single Line Chart
            var ctx7 = $("#line-chart").get(0).getContext("2d");
            var myChart7 = new Chart(ctx7, {
                type: "line",
                data: {
                    labels: data.purchased_year,
                    datasets: [{
                        label: "Sales",
                        fill: false,
                        backgroundColor: "rgba(0, 156, 255, .3)",
                        data: data.num_vip_users_year
                    }]
                },
                options: {
                    responsive: true
                }
            });
            
            // Single Line Chart
            var ctx8 = $("#line-chart-2").get(0).getContext("2d");
            var myChart8 = new Chart(ctx8, {
                type: "line",
                data: {
                    labels: data.purchased_month,
                    datasets: [{
                        label: "Sales",
                        fill: false,
                        backgroundColor: "rgba(0, 156, 255, .3)",
                        data: data.num_vip_users_month
                    }]
                },
                options: {
                    responsive: true
                }
            });

        }
    });

})(jQuery);

// Define a function to retrieve the selected value from the dropdown
function getData() {
    var selected = document.getElementById("dropdown").value;
    console.log('Selected option:', selected);
    return selected;
}

// Function to update the chart
function updateChart() {
    var selectedValue = getData(); // Get the selected value from the dropdown

    // Perform AJAX request to fetch data based on the selected value
    $.ajax({
        url: '/time_series_on_exam_id',
        type: 'GET',
        success: function(data) {
            // Check if the selected value exists in the "exam_name" array
            var selectedIndex = data.exam_name.indexOf(selectedValue);
            
            // Extract data for the selected exam ID
            const duration = data.duration[selectedIndex]; // Define the duration in minutes
            const minuteArray = []; // Create an array to store each minute
            for (let minute = 0; minute <= duration; minute++) {
                minuteArray.push(minute);}

            // Update chart with new data
            var ctx4 = $("#salse-revenue").get(0).getContext("2d");
            if (window.myChart4) {
                window.myChart4.destroy(); // Destroy previous chart instance if it exists
            }
            window.myChart4 = new Chart(ctx4, {
                type: "line",
                data: {
                    labels: minuteArray,
                    datasets: [{
                            label: "Normal",
                            data: data.number_of_normal[selectedIndex],
                            backgroundColor: "rgba(0, 156, 255, .5)",
                            fill: true
                        },
                        {
                            label: "Abnormal",
                            data: data.number_of_abnormal[selectedIndex],
                            backgroundColor: "rgba(255, 0, 0, .3)",
                            fill: true
                        }
                    ]
                },
                options: {
                    responsive: true
                }
            });
        }
    });
}

// Call the updateChart function when the dropdown value changes
document.getElementById("dropdown").addEventListener("change", function() {
    updateChart();
});

// Initially load the chart with the default selected value
updateChart();
