program PetyaAndStrings;
(* https://codeforces.com/problemset/problem/112/A *)
uses sysutils;
var line_a, line_b: String;
begin
	ReadLn(line_a);
	ReadLn(line_b);
	writeln(AnsiCompareText(line_a, line_b));
end.
