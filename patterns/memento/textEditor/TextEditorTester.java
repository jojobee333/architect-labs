package patterns.memento.textEditor;

/**
 * Simple tester class for {@link TextEditor}. Runs a few operations and
 * prints the state to stdout so you can verify that saving and restoring
 * via the memento works correctly.
 */
public class TextEditorTester {
    public static void main(String[] args) {
        TextEditor editor = new TextEditor();
        System.out.println("Initial content: '" + editor.read() + "'");

        editor.write("Hello");
        System.out.println("After writing 'Hello': '" + editor.read() + "'");

        // save state
        TextEditor.EditorState snapshot = editor.save();

        editor.write(" World!");
        System.out.println("After additional write: '" + editor.read() + "'");

        // restore previous state
        editor.restore(snapshot);
        System.out.println("After restore: '" + editor.read() + "'");

        // another change
        editor.write(" Again.");
        System.out.println("Final content: '" + editor.read() + "'");
    }
}
