## Eventual method to assign pivots rather than randomly
<ul>
	<li>Calculate the initial pivot as an average of all the existing points</li>
	<li>Select the next pivot such that the initial already assigned pivots are situated at a max distance from it</li>
	<li>Continue assigning pivots until all are assigned</li>
</ul>

## Other heuristics to initialize pivots
<p>???</p>

## Can t1, ..., tc satisfy some other value of oi than m/2? 
<p>???</p>

## Experiment with:
<ul>
	<li>the convergence rate</li>
	<li>the error tolerances</li>
</ul>

## Anything to do about... ?
<ul>
	<li>The accumulated force</li>
	<li>The individual forces</li>
</ul>

## Eventual distance measures
<p>Binary similarity distance measures: http://www.baskent.edu.tr/~hogul/binary.pdf</p>
<p>Others, but probably not for us:</p>
<ul>
	<li>Hamming distance HD</li>
	<li>normalized Hamming distance NHD</li>
	<li>asymmetric Hamming distance AHD</li>
	<li>weighted Hamming distance WHD</li>
	<li>query-dependent weighted Hamming distance QWHD</li>
	<li>normalized Hamming affinity NHA</li>
	<li>Manhattan MD</li>
	<li>asymmetric Euclidean distance AED</li>
	<li>symmetric Euclidean distance SED</li>
	<li>lower bound LB</li>
</ul>


## Evaluation
<ul>
	<li>precision vs. recall</li>
	<li>...</li>
</ul>


## Some more links
<ul>
	<li>
		paper that kind of += previous papers: http://cgis.cs.umd.edu/grad/scholarlypapers/papers/Bondugula.pdf
	</li>
	<li>
		spherical hashing paper -- version 2 (same as version 1, but with some more pics): https://pdfs.semanticscholar.org/81c7/bfa5dfd5401a4a6208a0d225c3e369e5bf56.pdf <br>
				(the pics can be seen here as well: 
					https://www.semanticscholar.org/paper/Spherical-Hashing-Binary-Code-Embedding-with-Heo-Lee/81c7bfa5dfd5401a4a6208a0d225c3e369e5bf56)
	</li>
</ul>






