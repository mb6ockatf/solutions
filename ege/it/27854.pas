Program TwopSevenEightFiveFour;
(* https://inf-ege.sdamgia.ru/problem?id=27854 *)
var
	i, j, div_number: longint;
	result_array: array[1..4] of longint;
begin
	for i := 110203 to 110245 do begin
		div_number := 0;
		for j := 2 to i do begin
			if (i mod j = 0) and (j mod 2 = 0) then begin
				div_number := div_number + 1;
				if div_number > 4 then break;
				result_array[div_number] := j;
			end;
		end;
		if div_number = 4 then begin
			writeln(result_array[1], ' ', result_array[2], ' ',
			result_array[3], ' ', result_array[4]);
		end;
	end;
end.
