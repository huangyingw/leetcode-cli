public class WordDictionary
{
  class TrieNode
  {
    char content;
    boolean isEnd;
    LinkedList<TrieNode> childNode;

    public TrieNode()
    {
      this.content = ' ';
      this.isEnd = false;
      this.childNode = new LinkedList<TrieNode>();
    }

    public TrieNode(char content)
    {
      this.content = content;
      this.isEnd = false;
      this.childNode = new LinkedList<TrieNode>();
    }

    public TrieNode subNode(char content)
    {
      if (childNode != null)
      {
        for (TrieNode node : childNode)
        {
          if (node.content == content)
          {
            return node;
          }
        }
      }

      return null;
    }

  }

  public class Trie
  {
    private TrieNode root;

    public Trie()
    {
      root = new TrieNode();
    }

    // Inserts a word into the trie.
    public void insert(String word)
    {
      TrieNode current = root;

      for (int i = 0; i < word.length(); i++ )
      {
        char c = word.charAt(i);
        TrieNode node = current.subNode(c);

        if (node == null)
        {
          current.childNode.add(new TrieNode(c));
          node = current.subNode(c);
        }

        current = node;
      }

      current.isEnd = true;
    }

    // Returns if the word is in the trie.
    public boolean search(String word, TrieNode root)
    {
      TrieNode current = root;

      for (int i = 0; i < word.length(); i++ )
      {
        if (word.charAt(i) == '.')
        {
          for (TrieNode trieNode : current.childNode)
          {
            if (search(word.substring(i), trieNode))
            {
              return true;
            }
          }

          return false;
        }
        else
        {
          TrieNode node = current.subNode(word.charAt(i));

          if (node == null)
          {
            return false;
          }

          current = node;
        }
      }

      if (current.isEnd == false)
      {
        return false;
      }
      else
      {
        return true;
      }
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    public boolean startsWith(String prefix)
    {
      TrieNode current = root;

      for (int i = 0; i < prefix.length(); i++ )
      {
        TrieNode node = current.subNode(prefix.charAt(i));

        if (node == null)
        {
          return false;
        }

        current = node;
      }

      return true;
    }
  }

  private Trie trie = new Trie();

  public void addWord(String word)
  {
    trie.insert(word);
  }

  public boolean search(String word)
  {
    return trie.search(word, trie.root);
  }
}

