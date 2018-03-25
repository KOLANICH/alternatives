__author__="KOLANICH"
__license__="Unlicense"
__copyright__=r"""
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org/>
"""
import typing, types

class SlottyRepr:
	"""Just a base class automatically generating __repr__"""
	__slots__=tuple()
	def __repr__(self):
		return "".join(( self.__class__.__name__, "(" , ", ".join(( "=".join((k, repr(getattr(self, k)))) for k in self.__class__.__slots__)), ")" ))

class Dependency(SlottyRepr):
	"""Represents a dependent package with some info how to get it"""
	__slots__=("name", "uri")
	def __init__(self, name:str, uri:str=None):
		self.name=name
		self.uri=uri

import importlib
class Alternative(SlottyRepr):
	"""Represents an alternative piece of API."""
	__slots__=("dependency", "funcName", "decorator")
	def __init__(self, dependency:Dependency, funcName:str, decorator:typing.Callable[[],types.ModuleType]=None):
		self.dependency=dependency
		self.funcName=funcName
		self.decorator=decorator
	def __call__(self, *args, **kwargs):
		r=importlib.import_module(self.dependency.name, None, *args, **kwargs)
		if self.funcName:
			r=getattr(r, self.funcName)
		if self.decorator:
			return self.decorator(r)
		return r

class AlternativezError(ImportError):
	"""Failed to import any of alternatives."""
	def __init__(self, msg:str, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.msg=msg

class Alternativez(SlottyRepr):
	"""The main class doing selection"""
	__slots__=("alternatives",)
	def __init__(self, alternatives:typing.Tuple[Alternative]):
		self.alternatives=alternatives
	def showHelp(self):
		msg="Please install anything of the following:\n"
		maxLen=max((len(alt.dependency.name) for alt in self.alternatives))
		for alt in self.alternatives:
			msg+="\t"+ alt.dependency.name+(":"+"\t"*((maxLen-len(alt.dependency.name))//4)+"\t"+alt.dependency.uri if alt.dependency.uri else "")+"\n"
		raise AlternativezError(msg, *self.alternatives)
	def __call__(self):
		for alt in self.alternatives:
			try:
				return alt()
			except ImportError:
				continue
		self.showHelp()

