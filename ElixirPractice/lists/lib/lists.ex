defmodule Lists do
  # [ ]
  def len([]), do: 0
  def len([_h|t]), do: 1 + len(t)

  def sum([]), do: 0
  def sum([h|t]), do: h + sum(t)

  def double([]), do: []
  def double([h|t]), do: [ 2*h | double(t) ]

  def square([]), do: []
  def square([h|t]), do: [ h*h | square(t) ]

  def map([], _func), do: []
  def map([h|t], func) do
    [ func.(h) | map(t, func) ]
  end
end
