Program TwoEightOneTwoZero;
var
	i, j, div_number: longint;
	res: array[1..4] of longint;
begin
	for i := 201455 to 201470 do begin
		div_number := 2; (* 1 and i included by default *)
		res[4] := i;
		for j := 2 to (i div 2) do begin
			if (i mod j <> 0) then begin
				continue;
			end;
			div_number := div_number + 1;
			if div_number > 4 then begin
				break;
			end;
			res[div_number - 1] := j;
		end;
		if div_number = 4 then begin
			writeln(1, ' ', res[2], ' ', res[3], ' ', res[4]);
		end;
	end;
end.
