/*
name : countTime.js
*/
(function($){
	var opt,ele,top;

	$.fn.countTime = function(option){
		ele = $(this);
		opt = option;
		date = strToTime(opt.time);

		// overtimeStop flag save in localstorage and overtimeStop event add
		localStorage.setItem("overtimePay", "");
		document.getElementById("overtimeStopButton").addEventListener("click", function (e) {
			overtimeStopFlag = localStorage.getItem("overtimeStop");
			if (overtimeStopFlag == "yes") {
				localStorage.setItem("overtimeStop", "no");
			} else {
				localStorage.setItem("overtimeStop", "yes");
			}
		});
		// end

		timePrint();

		setInterval(function(){timePrint();},1000);


		function strToTime(str){

			y = parseInt(str.substr(0,4));
			m = parseInt(str.substr(5,2))-1;
			d = parseInt(str.substr(8,2));
			h = parseInt(str.substr(11,2));
			i = parseInt(str.substr(14,2));
			s = parseInt(str.substr(17,2));

			tmp = new Date(y,m,d,h,i,s);

			return sec(tmp);
		}
		
		function timeToStr(sec){

			str = '';

			d = Math.floor(sec/(60*60*24));
			mod = (sec%(60*60*24));

			h = addZero(Math.floor(mod/(60*60)),2);
			mod = (mod%(60*60));

			i = addZero(Math.floor(mod/60),2);
			mod = (mod%60);

			s = addZero(Math.floor(mod),2);

			if(d!=0) str = (d*(-1))+'Day ';

			if(h<0) h = addZero(h*(-1),2);
			if(s<0) s = addZero(s*(-1),2);

			str += h+':'+i+':'+s;

			return str;
		}

		function sec(date){
			return Math.floor(date.getTime()/1000);
		}

		function addZero(data, len) {
			data= '000000000000000'+data;
			return data.substr(data.length - len, len);
		}
		
		// 시급 계산 : 2018 시급- 7530원, 야간 1.5배 11295원
		// 분당 188.25원 초당 3.1375원

		function overtimeCalc(flag, result) {
			if (flag) {
				overtimePay = result * 3.1375;
				localStorage.setItem("overtimePay", overtimePay);
			}
			document.getElementById("overtimePay").innerText = Math.floor(localStorage.getItem("overtimePay"));
		}

		function timePrint(){
		    Now = new Date();
			now = sec(Now);
			result = date-now;
			overtimeStopFlag = localStorage.getItem("overtimeStop");

            if (Now.getHours() >= 18 || Now.getHours()<8) {
				document.getElementById("afterTime").style.display = "block";
				if(overtimeStopFlag == "yes") {
					document.getElementById("beforeTime").style.color = "#212529";
					result = "퇴근했습니다.";
					ele.empty();
					ele.append(result);
					overtimeCalc(0, "");
				} else {
					document.getElementById("beforeTime").style.color = "#dd4b39";
					result = now-date;
					ele.empty();
					ele.append(timeToStr(result));
					overtimeCalc(1, result);
				}
            } else {
				if (overtimeStopFlag == "yes") {
					localStorage.setItem("overtimeStop", "no");
				} 
				document.getElementById("afterTime").style.display = "none";
                ele.empty();
                ele.append(timeToStr(result));
            }
		}
	}
})(jQuery);
