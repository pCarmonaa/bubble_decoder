from typing import Any, Dict, Set
import json
from datetime import datetime, date
from decimal import Decimal


class GenericObjectSerializer:
    """
    A generic serializer that converts any Python object to JSON-serializable dictionary
    without requiring changes to domain models or adding dependencies to the domain layer.
    
    Uses reflection to automatically discover object attributes and handles:
    - Nested objects
    - Collections (lists, tuples, sets)
    - Dictionaries
    - Primitive types
    - Custom objects with __dict__
    - Circular references prevention
    """
    
    @staticmethod
    def to_dict(obj: Any, _visited: Set[int] = None) -> Dict[str, Any]:
        """
        Converts any object to a JSON-serializable dictionary.
        
        Args:
            obj: The object to serialize
            _visited: Internal parameter to prevent circular references
            
        Returns:
            Dictionary representation of the object
        """
        if _visited is None:
            _visited = set()
        
        if obj is None:
            return None
        
        if isinstance(obj, (str, int, float, bool)):
            return obj
        
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        
        if isinstance(obj, Decimal):
            return float(obj)
        
        if isinstance(obj, (list, tuple)):
            return [GenericObjectSerializer.to_dict(item, _visited) for item in obj]
        
        if isinstance(obj, set):
            return [GenericObjectSerializer.to_dict(item, _visited) for item in obj]
        
        if isinstance(obj, dict):
            return {
                key: GenericObjectSerializer.to_dict(value, _visited) 
                for key, value in obj.items()
            }
        
        obj_id = id(obj)
        if obj_id in _visited:
            return f"<Circular reference to {type(obj).__name__}>"
        
        _visited.add(obj_id)
        
        try:
            if hasattr(obj, '__dict__'):
                result = {}
                for key, value in obj.__dict__.items():
                    if not key.startswith('_') and not callable(value):
                        result[key] = GenericObjectSerializer.to_dict(value, _visited)
                return result
            
            elif hasattr(obj, '__slots__'):
                result = {}
                for slot in obj.__slots__:
                    if hasattr(obj, slot):
                        value = getattr(obj, slot)
                        if not callable(value):
                            result[slot] = GenericObjectSerializer.to_dict(value, _visited)
                return result
            
            else:
                return str(obj)
                
        finally:
            _visited.remove(obj_id)
    
    @staticmethod
    def to_json(obj: Any, indent: int = None) -> str:
        """
        Converts any object directly to JSON string.
        
        Args:
            obj: The object to serialize
            indent: JSON indentation (None for compact, 2 for pretty)
            
        Returns:
            JSON string representation
        """
        return json.dumps(
            GenericObjectSerializer.to_dict(obj),
            ensure_ascii=False,
            indent=indent,
            default=str
        ) 