string = '''Java is a general-purpose computer programming language that is concurrent,
class-based, object-oriented,[14] and specifically designed to have as few
implementation dependencies as possible. It is intended to let application
developers write once, run anywhere (WORA),[15] meaning that compiled Java
code can run on all platforms that support Java without the need for
recompilation.[16] Java applications are typically compiled to bytecode that can
run on any Java virtual machine (JVM) regardless of computer architecture. As of
2016, Java is one of the most popular programming languages in
use,[17][18][19][20] particularly for client-server web applications, with a
reported 9 million developers.[21] Java was originally developed by James
Gosling at Sun Microsystems (which has since been acquired by Oracle
Corporation) and released in 1995 as a core component of Sun Microsystems' Java
platform. The language derives much of its syntax from C and C++, but it has
fewer low-level facilities than either of them.

The original and reference implementation Java compilers, virtual machines, and
class libraries were originally released by Sun under proprietary licences. As
of May 2007, in compliance with the specifications of the Java Community
Process, Sun relicensed most of its Java technologies under the GNU General
Public License. Others have also developed alternative implementations of these
Sun technologies, such as the GNU Compiler for Java (bytecode compiler), GNU
Classpath (standard libraries), and IcedTea-Web (browser plugin for applets).

The latest version is Java 8, which is the only version currently supported for
free by Oracle, although earlier versions are supported both by Oracle and other
companies on a commercial basis.

James Gosling, Mike Sheridan, and Patrick Naughton initiated the Java language
project in June 1991.[22] Java was originally designed for interactive
television, but it was too advanced for the digital cable television industry at
the time.[23] The language was initially called Oak after an oak tree that stood
outside Gosling's office. Later the project went by the name Green and was
finally renamed Java, from Java coffee.[24] Gosling designed Java with a
C/C++-style syntax that system and application programmers would find
familiar.[25]

Sun Microsystems released the first public implementation as Java 1.0 in
1995.[26] It promised Write Once, Run Anywhere (WORA), providing no-cost
run-times on popular platforms. Fairly secure and featuring configurable
security, it allowed network- and file-access restrictions. Major web browsers
soon incorporated the ability to run Java applets within web pages, and Java
quickly became popular, while mostly outside of browsers, that wasn't the
original plan. In January 2016, Oracle announced that Java runtime environments
based on JDK 9 will discontinue the browser plugin.[27] The Java 1.0 compiler
was re-written in Java by Arthur van Hoff to comply strictly with the Java 1.0
language specification.[28] With the advent of Java 2 (released initially as
built for different types of platforms. J2EE included technologies and APIs for
enterprise applications typically run in server environments, while J2ME
featured APIs optimized for mobile applications. The desktop version was renamed
J2SE. In 2006, for marketing purposes, Sun renamed new J2 versions as Java EE,
Java ME, and Java SE, respectively.

In 1997, Sun Microsystems approached the ISO/IEC JTC 1 standards body and later
the Ecma International to formalize Java, but it soon withdrew from the
process.[29][30][31] Java remains a de facto standard, controlled through the
Java Community Process.[32] At one time, Sun made most of its Java
implementations available without charge, despite their proprietary software
status. Sun generated revenue from Java through the selling of licenses for
specialized products such as the Java Enterprise System.

On November 13, 2006, Sun released much of its Java virtual machine (JVM) as
free and open-source software, (FOSS), under the terms of the GNU General Public
License (GPL). On May 8, 2007, Sun finished the process, making all of its JVM's
core code available under free software/open-source distribution terms, aside
from a small portion of code to which Sun did not hold the copyright.[33]

Sun's vice-president Rich Green said that Sun's ideal role with regard to Java
was as an ;evangelist;.[34] Following Oracle Corporation's acquisition of Sun
lawsuit against Google shortly after that for using Java inside the Android SDK
(see Google section below). Java software runs on everything from laptops to
data centers, game consoles to scientific supercomputers.[36] On April 2, 2010,
James Gosling resigned from Oracle.

One design goal of Java is portability, which means that programs written for
the Java platform must run similarly on any combination of hardware and
operating system with adequate runtime support. This is achieved by compiling
the Java language code to an intermediate representation called Java bytecode,
instead of directly to architecture-specific machine code. Java bytecode
instructions are analogous to machine code, but they are intended to be executed
by a virtual machine (VM) written specifically for the host hardware. End users
commonly use a Java Runtime Environment (JRE) installed on their own machine for
standalone Java applications, or in a web browser for Java applets.

Standard libraries provide a generic way to access host-specific features such
as graphics, threading, and networking.

The use of universal bytecode makes porting simple. However, the overhead of
interpreting bytecode into machine instructions makes interpreted programs
almost always run more slowly than native executables. However, just-in-time
(JIT) compilers that compile bytecodes to machine code during runtime were
introduced from an early stage. Java itself is platform-independent, and is
adapted to the particular platform it is to run on by a Java virtual machine for
it, which translates the Java bytecode into the platform's machine language.

Oracle Corporation is the current owner of the official implementation of the
Java SE platform, following their acquisition of Sun Microsystems on January 27,
2010. This implementation is based on the original implementation of Java by
Sun. The Oracle implementation is available for Microsoft Windows (still works
for XP, while only later versions currently ;publicly; supported), Mac OS X,
Linux and Solaris. Because Java lacks any formal standardization recognized by
Ecma International, ISO/IEC, ANSI, or other third-party standards organization,
the Oracle implementation is the de facto standard.

The Oracle implementation is packaged into two different distributions: The Java
Runtime Environment (JRE) which contains the parts of the Java SE platform
required to run Java programs and is intended for end users, and the Java
Development Kit (JDK), which is intended for software developers and includes
development tools such as the Java compiler, Javadoc, Jar, and a debugger.

OpenJDK is another notable Java SE implementation that is licensed under the GNU
GPL. The implementation started when Sun began releasing the Java source code
under the GPL. As of Java SE 7, OpenJDK is the official Java reference
implementation.

The goal of Java is to make all implementations of Java compatible.
Historically, Sun's trademark license for usage of the Java brand insists that
all implementations be ;compatible;. This resulted in a legal dispute with
Microsoft after Sun claimed that the Microsoft implementation did not support
RMI or JNI and had added platform-specific features of their own. Sun sued in
1997, and in 2001 won a settlement of US$20 million, as well as a court order
enforcing the terms of the license from Sun.[39] As a result, Microsoft no
longer ships Java with Windows.

Platform-independent Java is essential to Java EE, and an even more rigorous
validation is required to certify an implementation. This environment enables
portable server-side applications.

Programs written in Java have a reputation for being slower and requiring more
memory than those written in C++.[40][41] However, Java programs' execution
speed improved significantly with the introduction of just-in-time compilation
in 1997/1998 for Java 1.1,[42] the addition of language features supporting
better code analysis (such as inner classes, the StringBuilder class, optional
assertions, etc.), and optimizations in the Java virtual machine, such as
HotSpot becoming the default for Sun's JVM in 2000. With Java 1.5, the
performance was improved with the addition of the java.util.concurrent package,
including Lock free implementations of the ConcurrentMaps and other multi-core
collections, and it was improved further Java 1.6.

Some platforms offer direct hardware support for Java; there are
microcontrollers that can run Java in hardware instead of a software Java
virtual machine, and ARM based processors can have hardware support for
executing Java bytecode through their Jazelle option (while its support is
mostly dropped in current implementations of ARM).

Java uses an automatic garbage collector to manage memory in the object
lifecycle. The programmer determines when objects are created, and the Java
runtime is responsible for recovering the memory once objects are no longer in
use. Once no references to an object remain, the unreachable memory becomes
eligible to be freed automatically by the garbage collector. Something similar
to a memory leak may still occur if a programmer's code holds a reference to an
object that is no longer needed, typically when objects that are no longer
needed are stored in containers that are still in use. If methods for a
nonexistent object are called, a ;null pointer exception; is thrown.[43][44]

One of the ideas behind Java's automatic memory management model is that
programmers can be spared the burden of having to perform manual memory
management. In some languages, memory for the creation of objects is implicitly
allocated on the stack, or explicitly allocated and deallocated from the heap.
In the latter case the responsibility of managing memory resides with the
programmer. If the program does not deallocate an object, a memory leak occurs.
If the program attempts to access or deallocate memory that has already been
deallocated, the result is undefined and difficult to predict, and the program
is likely to become unstable and/or crash. This can be partially remedied by the
use of smart pointers, but these add overhead and complexity. Note that garbage
collection does not prevent ;logical; memory leaks, i.e., those where the memory
is still referenced but never used.

Garbage collection may happen at any time. Ideally, it will occur when a program
is idle. It is guaranteed to be triggered if there is insufficient free memory
on the heap to allocate a new object; this can cause a program to stall
momentarily. Explicit memory management is not possible in Java.

Java does not support C/C++ style pointer arithmetic, where object addresses and
unsigned integers (usually long integers) can be used interchangeably. This
allows the garbage collector to relocate referenced objects and ensures type
safety and security.

As in C++ and some other object-oriented languages, variables of Java's
primitive data types are either stored directly in fields (for objects) or on
the stack (for methods) rather than on the heap, as is commonly true for
non-primitive data types (but see escape analysis). This was a conscious
decision by Java's designers for performance reasons.

Java contains multiple types of garbage collectors. By default,[citation needed]
HotSpot uses the parallel scavenge garbage collector. However, there are also
several other garbage collectors that can be used to manage the heap. For 90% of
applications in Java, the Concurrent Mark-Sweep (CMS) garbage collector is
sufficient.[45] Oracle aims to replace CMS with the Garbage-First collector
(G1).'''
