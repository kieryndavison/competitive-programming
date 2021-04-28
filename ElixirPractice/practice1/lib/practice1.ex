defmodule Practice1 do
  def test1({ a, b }), do: {b, a} 
  def match({a, a}), do: true
  def match({_, _}), do: false
end
