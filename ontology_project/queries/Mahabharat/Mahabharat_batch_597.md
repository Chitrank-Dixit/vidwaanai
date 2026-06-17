# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Mahabharat 0.5961)
- **Original**: 210 संक्षिप्त महाभारत 4 [ झाक्तिपर्त धर्म, अर्थ और कामका भोग करो। पीछे प्रसन्नतासे बनमें
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5961)
- **Original**: 210 संक्षिप्त महाभारत 4 [ झाक्तिपर्त धर्म, अर्थ और कामका भोग करो। पीछे प्रसन्नतासे बनमें
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5962)
- **Original**: दुर्दा्त (कर) कहा जाता है। कई बार प्रजा स्त्रेण जो राजाकी चले जाना। पहले अतिथियों, पितरों और देवताओंके ऋणसे
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5962)
- **Original**: दुर्दा्त (कर) कहा जाता है। कई बार प्रजा स्त्रेण जो राजाकी चले जाना। पहले अतिथियों, पितरों और देवताओंके ऋणसे
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5963)
- **Original**: ओरसे सुरक्षित न होनेके कारण अनावृष्टि आदि: दैवीः उ्लण हो लो, इसके बाद यह सब करना । अभी तो सर्वमेध
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5963)
- **Original**: ओरसे सुरक्षित न होनेके कारण अनावृष्टि आदि: दैवीः उ्लण हो लो, इसके बाद यह सब करना । अभी तो सर्वमेध
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5964)
- **Original**: आपत्तियोंसे नष्ट हो जाते हैं तथा चोरोंके उपद्रवादिसे और अश्वमेथ यज्ञोंका अनुष्ठान करो। यदि तुम अपने
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5964)
- **Original**: आपत्तियोंसे नष्ट हो जाते हैं तथा चोरोंके उपद्रवादिसे और अश्वमेथ यज्ञोंका अनुष्ठान करो। यदि तुम अपने
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5965)
- **Original**: दुःख पाते हैं, उसमें राजा ही दोषका भागी होता है। किंतु भाइयोंके साथ बड़ी-बड़ी दक्षिणाओंवाले यज्ञ करेगे तो तुम्हें
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5965)
- **Original**: दुःख पाते हैं, उसमें राजा ही दोषका भागी होता है। किंतु भाइयोंके साथ बड़ी-बड़ी दक्षिणाओंवाले यज्ञ करेगे तो तुम्हें
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5966)
- **Original**: पूरे-पूरे विचार और नीतिके साथ सब प्रकार प्रयत्न करनेपर अतुलित यज्ष प्राप्त होगा
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5966)
- **Original**: पूरे-पूरे विचार और नीतिके साथ सब प्रकार प्रयत्न करनेपर अतुलित यज्ष प्राप्त होगा
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5967)
- **Original**: राजन्‌ ! मैं तुमसे जो बात कहता
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5967)
- **Original**: राजन्‌ ! मैं तुमसे जो बात कहता
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5968)
- **Original**: भी यदि सफलता न मिले तो उस अवस्थामें राजाको कोई हूँ:उसपर ध्यान दो। जैसा करनेसे तुम अपने धर्मसे नहीं
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5968)
- **Original**: भी यदि सफलता न मिले तो उस अवस्थामें राजाको कोई हूँ:उसपर ध्यान दो। जैसा करनेसे तुम अपने धर्मसे नहीं
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5969)
- **Original**: पाप नहीं होता। गिणेगे। देखो, जो राजा करका छठा भाग लेकर भी राष्ट्रकी *राजन्‌ ! इस विषययें मैं तुम्हें हयप्रीवका प्रसंग सुनाता रक्षा नहीं करता वह अपनी प्रजाके चतुर्थांश पापका भागी
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5969)
- **Original**: पाप नहीं होता। गिणेगे। देखो, जो राजा करका छठा भाग लेकर भी राष्ट्रकी *राजन्‌ ! इस विषययें मैं तुम्हें हयप्रीवका प्रसंग सुनाता रक्षा नहीं करता वह अपनी प्रजाके चतुर्थांश पापका भागी
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5970)
- **Original**: हूँ। वह बड़ा शूरवीर और पवित्र कर्म करनेवाल्ता था। उसने बनता है। यदि राजा धर्मझाखका उल्लदून करता है तो पतित
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5970)
- **Original**: हूँ। वह बड़ा शूरवीर और पवित्र कर्म करनेवाल्ता था। उसने बनता है। यदि राजा धर्मझाखका उल्लदून करता है तो पतित
- **Translation**: 

---

