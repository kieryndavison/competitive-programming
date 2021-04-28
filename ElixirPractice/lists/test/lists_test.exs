defmodule ListsTest do
  use ExUnit.Case
  doctest Lists

  test "greets the world" do
    assert Lists.hello() == :world
  end
end
