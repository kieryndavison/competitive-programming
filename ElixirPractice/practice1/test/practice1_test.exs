defmodule Practice1Test do
  use ExUnit.Case
  doctest Practice1

  test "greets the world" do
    assert Practice1.hello() == :world
  end
end
