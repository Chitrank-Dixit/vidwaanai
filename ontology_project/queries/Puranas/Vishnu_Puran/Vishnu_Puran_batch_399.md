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

### Verse 1 (Vishnu Puran 0.7961)
- **Original**: आर्य बल्भद्रकों भी इसके कारणसे मदिशापान आदि सम्पूर्ण भोगोंको त्यागना पड़ेगा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7962)
- **Original**: इसलिये हे दानपते
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7963)
- **Original**: -ये यादवराण, बलभद्रजो, मैं और सत्यभामा सब्र मिलकर आपसे प्रार्थना करते हैं कि इसे धारण करनेगें आप ही समर्थ हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7964)
- **Original**: 158-159
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7965)
- **Original**: आपके धारण करनेसे यह सम्पूर्ण राष्ट्रका हित करेगी, इसलिये सम्पूर्ण गष्ट्रके मड्जलके लिये आप ही इसे पूर्बबत्‌ घारण कीजिये; इस लिफयमे आप और कुछ भी न कहें ।'' भगबान्‌के ऐसा कहनेपर दानपति अक्रूरने 'जो आज्ञा' कह बह महारत्र ले लिया। तबसे अक्रूरजी सबके सामने डस अति देदीप्यमान मणिकों मपने गलेमें धारणकर सुर्यके समान क्विरण-जालसे युक्त होकर लिचरते लगे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7966)
- **Original**: 160-161
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7967)
- **Original**: भगवानके मिथ्या-कल्डू-शांधनरूप इस प्रसड्राका जो कोई स्मरण करेगा उसे कभी थोड़ा-सा भी मिंध्या कलडुू न लगेगा, उसकी समस्त इच्द्रियाँ समर्थ रहेंगी तथा वह समस्त पापोंसे मुक्त हो जावगा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7968)
- **Original**: चल» जी पा इति श्रीविष्णुपुराणे चतुर्थेउदों त्रयोदशोउध्याय:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7969)
- **Original**: आ* 14 ] चतुर्थ अंदा 281 चोदहवाँ अध्याय अनपभित्र और अन्धकके बंशका वर्णन औपराजर उवाच अनमित्रस्थ पुत्र: शिनिर्नामाभवत्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7970)
- **Original**: तस्थापि सत्यकः सत्यकात्सात्यकिर्युयुधानापर- नामा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7971)
- **Original**: तस्मादपि सल्भयः तत्पुन्नअ्र कुणि: कुणेर्युगबधर:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7972)
- **Original**: इत्येते दैनेया:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7973)
- **Original**: अनमित्रस्यान्वये पृश्निस्तस्मात्‌ श्वफल्क:ः तत्पभाव: कथित एव
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7974)
- **Original**: श्रफल्कस्थान्यः कनीयांख्िश्रको नाम भ्राता
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7975)
- **Original**: श्रफल्का- दक्कूरो गान्दिन्यामभवत्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7976)
- **Original**: तथोपमदु- धर्मदृग्दृष्टधर्मगन्‍्धमोजवाहप्रतिवाहाख्या: पुत्रा:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7977)
- **Original**: सुताराख्या कन्या च
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7978)
- **Original**: देवबानुपदेवश्चाक््रपुत्रौ
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7979)
- **Original**: पृथुविपृथु- प्रमुस्ाश्नित्रकस्य पुत्रा बहतो बरभूखु:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7980)
- **Original**: कुक्रभजमानशुचिकम्बलबर्हिषा ख्या- स्तथानलथकस्य चत्वार: पुत्रा:
- **Translation**: 

---

