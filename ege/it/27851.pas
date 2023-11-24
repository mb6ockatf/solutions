Program TwoSevenEightFiveOne;
(* https://inf-ege.sdamgia.ru/problem?id=27851 *)
var
	number, division_numbers, j: longint;
	results_array: array[1..4] of longint;
begin
	for number := 210235 to 210300 do begin
		division_numbers := 0;
		for j := 2 to number div 2 do begin
			if (number mod j) = 0 then begin
				division_numbers := division_numbers + 1;
				if division_numbers > 4 then break;
				results_array[division_numbers] := j;
			end;
		end;
		if division_numbers <> 4 then continue;
		writeln(number, ' ', results_array[1], ' ', results_array[2],
			' ', results_array[3], ' ', results_array[4]);
	end;
end.
