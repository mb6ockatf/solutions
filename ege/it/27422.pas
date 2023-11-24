Program TwoSevenFourTwoTwo;
(* https://inf-ege.sdamgia.ru/problem?id=27422 *)
var
	division_number, i, j: longint;
	result_array: array[1..2] of longint;
begin
    for i := 174457 to 174505 do begin
	    division_number := 0;
	    for j := 2 to i div 2 do begin
		    if i mod j  = 0 then begin
			    division_number := division_number + 1;
			    if division_number > 2 then break;
			    result_array[division_number] := j;
		    end;
	    end;
	    if division_number = 2 then writeln(result_array[1], ' ',
		    result_array[2]);
    end;
end.

