# C++
## The Basics
Hello World
```cpp
#include <iostream>

int main() {
    std::cout << "Hello World!";
    return 0;
}
```

## Recent Interview
After a recent interview, there were a few specific things that tripped me up. C++ has a handful of different ways to do the same thing, so this is going to be a couple of those ways to do the same thing - or changes after a specific version of C++ that may be more often confused with alternatives within the language.

### Dereferencing a Pointer
```cpp
#include <iostream>
#include <stdio.h>
#include <vector>

int main() {
    std::vector v;
    //There are two different ways to do this
    (*v).insert(3);
    //and
    v->insert(3);
    //Both can be used to access members of a class or struct through a pointer
}
```

### vector.erase(const_sequentialindex)
What does this function do?

Well, pre-C++2011, this function performs a memcopy of a vector. std::copy copies elements from one range to another. Ex. if you have [1,2,3,4,5] and want to remove index 3 (number 4 in that vector), you'd essentially create a memcopy and keep both [1,2,3,4,5] and [1,2,3,5] in memory before destroying [1,2,3,4,5] later in memory.

At and after C++2011, this function call the move() function (provided below). This move function would;
- perform a 'memory lock' (conceptually) to prevent it from being accessed by more than 1 thread or process
- then validates that the range is valid (checks for buffer overflow concerns)
- finishing off the operation with a memory-move operation using `__copy_move_a2<true>`
   - where <true> indicates that this is a 'moving' operation (as opposed to copying)
   - Preventing your application's memory footprint from potentially "ballooning", or increasing by 2x-1 in size to perform this operation

([From libstdc++/stl_algobase.h:L475-L492](https://gcc.gnu.org/onlinedocs/gcc-4.6.3/libstdc++/api/a01046_source.html#l00475))
```cpp
00475   template<typename _II, typename _OI>
00476     inline _OI
00477     move(_II __first, _II __last, _OI __result)
00478     {
00479       // concept requirements
00480       __glibcxx_function_requires(_InputIteratorConcept<_II>)
00481       __glibcxx_function_requires(_OutputIteratorConcept<_OI,
00482         typename iterator_traits<_II>::value_type>)
00483       __glibcxx_requires_valid_range(__first, __last);
00484 
00485       return std::__copy_move_a2<true>(std::__miter_base(__first),
00486                        std::__miter_base(__last), __result);
00487     }
00488 
00489 #define _GLIBCXX_MOVE3(_Tp, _Up, _Vp) std::move(_Tp, _Up, _Vp)
00490 #else
00491 #define _GLIBCXX_MOVE3(_Tp, _Up, _Vp) std::copy(_Tp, _Up, _Vp)
00492 #endif
```
We also have this (below) that defines the erase function. Also found through [libstdc++/vector.tcc:L133](https://gcc.gnu.org/onlinedocs/gcc-4.6.3/libstdc++/api/a01117_source.html#l00133).
```cpp
00133   template<typename _Tp, typename _Alloc>
00134     typename vector<_Tp, _Alloc>::iterator
00135     vector<_Tp, _Alloc>::
00136     erase(iterator __position)
00137     {
00138       if (__position + 1 != end())
00139     _GLIBCXX_MOVE3(__position + 1, end(), __position);
00140       --this->_M_impl._M_finish;
00141       this->_M_impl.destroy(this->_M_impl._M_finish);
00142       return __position;
00143     }
```

Okay, now we should have everything we need to understand what's going on here. Basically, the erase function;
- checks to make sure the end is not at the next index
    - if we're removing the end function, then move the end of this vector to the current position and remove the pointer to the 'next' (current) index
- otherwise,
    - decrement the `this` pointer back 1 space in memory, updating the next iterator to the end of the vector
    - Then, the end of the vector is destroyed (memory is freed/reallocated)
    - Then the current index is returned

Essentially, this does not perform a memcopy on newer implementations of C++ after v11. A bit odd, but C++ is "more of a pointer language" as it were anyways..
