from stack import Stack

class TowerOfHanoi:
    """Tower of Hanoi puzzle implementation using stack data structure."""
    
    def __init__(self, num_disks):
        """Initialize Tower of Hanoi with specified number of disks."""
        self.num_disks = num_disks
        self.moves = 0
        # Initialize three stacks for the towers
        self.source = Stack(num_disks, "A")
        self.spare = Stack(num_disks, "B")
        self.target = Stack(num_disks, "C")
        
        # Initialize source stack with disks (larger disks at bottom)
        for disk in range(num_disks, 0, -1):
            self.source.push(disk)
            
    def move_disk(self, source, target):
        """Move one disk from source to target stack."""
        disk = source.pop()
        target.push(disk)
        self.moves += 1
        print(f"Move disk {disk} from {source.name} to {target.name}")
        self.display_state()
    
    def solve(self, n=None, source=None, target=None, spare=None):
        """Solve Tower of Hanoi recursively."""
        # Initialize parameters on first call
        if n is None:
            n = self.num_disks
            source = self.source    
            target = self.target
            spare = self.spare
            print(f"\nSolving Tower of Hanoi with {self.num_disks} disks")
            print("Initial state:")
            self.display_state()

        if n == 1:
            # Base case: move single disk from source to target
            self.move_disk(source, target)
        else:
            # Recursive case:
            # 1. Move n-1 disks from source to spare using target as spare
            # 2. Move largest disk from source to target
            # 3. Move n-1 disks from spare to target using source as spare
            self.solve(n - 1, source, spare, target)
            self.move_disk(source, target)
            self.solve(n - 1, spare, target, source)

    def display_state(self):
        """Display current state of all towers with proper formatting."""
        # Get the current state of all stacks
        source_disks = self.source.get_items()
        spare_disks = self.spare.get_items()
        target_disks = self.target.get_items()
        
        # Pad lists with empty spaces and reverse them for display (larger disks at bottom)
        max_height = self.num_disks
        source_disks = ['|'] * (max_height - len(source_disks)) + source_disks[::-1]
        spare_disks = ['|'] * (max_height - len(spare_disks)) + spare_disks[::-1]
        target_disks = ['|'] * (max_height - len(target_disks)) + target_disks[::-1]
        
        # Calculate the maximum width needed for display
        max_disk_width = self.num_disks * 2 + 1
        tower_spacing = 4
        total_width = (max_disk_width + tower_spacing) * 3
        
        print("\nCurrent State:")
        print(" " + "=" * total_width)
        
        # Display from top to bottom
        for level in range(max_height):
            # Create visual representation of disks with proper centering
            def disk_display(disk):
                if isinstance(disk, int):
                    disk_width = disk * 2 + 1
                    disk_str = "=" * disk_width
                    padding = (max_disk_width - disk_width) // 2
                    return " " * padding + disk_str + " " * padding
                return " " * ((max_disk_width - 1) // 2) + "|" + " " * ((max_disk_width - 1) // 2)
            
            source_display = disk_display(source_disks[level])
            spare_display = disk_display(spare_disks[level])
            target_display = disk_display(target_disks[level])
            
            # Print the level with proper spacing
            print(" " + source_display + " " * tower_spacing + 
                  spare_display + " " * tower_spacing + 
                  target_display)
        
        # Print tower bases and labels
        base_line = "=" * max_disk_width
        print(" " + base_line + " " * tower_spacing + 
              base_line + " " * tower_spacing + 
              base_line)
        
        # Center the tower labels under their bases
        label_padding = (max_disk_width - 1) // 2
        print(" " + " " * label_padding + "A" + " " * label_padding + " " * tower_spacing +
              " " * label_padding + "B" + " " * label_padding + " " * tower_spacing +
              " " * label_padding + "C" + " " * label_padding)
        print(" " + "=" * total_width)

def main():
    """Main function to run the Tower of Hanoi puzzle."""
    while True:
        try:
            num_disks = int(input("Enter the number of disks: "))
            if num_disks <= 0:
                print("Please enter a positive number.")
                continue
            
            # Create and solve puzzle
            tower = TowerOfHanoi(num_disks)
            tower.solve()
            
            print(f"\nPuzzle solved in {tower.moves} moves!")
            print(f"Minimum possible moves: {(2 ** num_disks) - 1}")
            break
            
        except ValueError:
            print("Please enter a valid integer number.")
            
if __name__ == "__main__":
    main()
