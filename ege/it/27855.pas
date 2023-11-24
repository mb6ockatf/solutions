Program TwoSevenEightFiveFive;
var
	i, j, div_number: longint;
	result_array: array[1..6] of longint;
begin
	for i := 95632 to 95650 do begin
		div_number := 0;
		for j := 1 to i do begin
			if (i mod j = 0) and (j mod 2 <> 0) then begin
				div_number := div_number + 1;
				if div_number > 6 then break;
				result_array[div_number] := j;
			end;
		end;
		if div_number = 6 then writeln(result_array[1], ' ',
			result_array[2], ' ', result_array[3], ' ',
			result_array[4], ' ', result_array[5], ' ',
			result_array[6]);
	end;
end.
