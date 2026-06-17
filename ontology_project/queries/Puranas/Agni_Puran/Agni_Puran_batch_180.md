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

### Verse 1 (Agni Puran 0.3581)
- **Original**: गूं शिखायै यषट्‌
- **Translation**: 

---

### Verse 2 (Agni Puran 0.3582)
- **Original**: मैं नेज़्त्रयाय वौषट्‌
- **Translation**: 

---

### Verse 3 (Agni Puran 0.3583)
- **Original**: गा कवचाय हुम्‌। ग: अस्काय फट ।'
- **Translation**: 

---

### Verse 4 (Agni Puran 0.3584)
- **Original**: कि ही के के के के के क कक के के के के के के क के कफ 7: 6 8 # 6 # क # के # 4 # 4 के के के । एक सौ अस्सीबाँ अध्याय पञ्ञमी तिथिके व्रत अग्निदेव कहते हैं-- वसिष्ठ! अब मैं आरोग्य,
- **Translation**: 

---

### Verse 5 (Agni Puran 0.3585)
- **Original**: मणिभद्र, ऐरावत, धृतराष्ट्, ककोटक और धनंजय स्वर्ग और मोक्ष प्रदान करेवाले पञ्षमी-क्रतका वर्णन
- **Translation**: 

---

### Verse 6 (Agni Puran 0.3586)
- **Original**: नामक नागोंका पूजन करना चाहिये
- **Translation**: 

---

### Verse 7 (Agni Puran 0.3587)
- **Original**: कर्ता हूँ। श्रावण, भद्दपद, आश्विन और कार्तिकके
- **Translation**: 

---

### Verse 8 (Agni Puran 0.3588)
- **Original**: ये सभी नाग अभय, आयु, विद्या, यश और शुक्लपक्षकी पञ्ममीको वासुकि, तक्षक, कालिय,
- **Translation**: 

---

### Verse 9 (Agni Puran 0.3589)
- **Original**: लक्ष्मी प्रदान करनेवाले हैं
- **Translation**: 

---

### Verse 10 (Agni Puran 0.3590)
- **Original**: इस ग्रकार आदि आग्लेय महापुराणमें 'प्ममीके ब्रतोंका वर्णन” तामक एक साँ अस्सीवाँ अभ्याय पूरा हुआ
- **Translation**: 

---

### Verse 11 (Agni Puran 0.3591)
- **Original**: #7000-वॉवनअ कर कक... एक सौ इक्यासीवाँ अध्याय षष्ठी तिथिके व्रत अग्निदेव कहते हैं--. अब मैं षष्ठी-सम्बन्धी
- **Translation**: 

---

### Verse 12 (Agni Puran 0.3592)
- **Original**: हैं। भाद्रपदके कृष्णपक्षकी षष्ठी तिथिमें ' अक्षयषष्ठी ख्रतोंको कहता हूँ। कार्तिकके कृष्णपक्षकी षष्ठीको
- **Translation**: 

---

### Verse 13 (Agni Puran 0.3593)
- **Original**: व्रत” करना चाहिये। इसे मार्गशीर्षमें भी करना 'फलमात्रका भोजन करके कार्तिकेयके लिये
- **Translation**: 

---

### Verse 14 (Agni Puran 0.3594)
- **Original**: चाहिये। इस अक्षयषष्ठीके दिन किसी भी एक अर्घ्यदान करना चाहिये। इससे मनुष्य भोग और
- **Translation**: 

---

### Verse 15 (Agni Puran 0.3595)
- **Original**: वर्ष निराहार रहनेसे मानव भोग और मोक्ष प्राप्त मोक्ष प्राप्त करता है। इसे “'स्कन्दषष्टी-ब्रत” कहते
- **Translation**: 

---

### Verse 16 (Agni Puran 0.3596)
- **Original**: कर लेता है
- **Translation**: 

---

### Verse 17 (Agni Puran 0.3597)
- **Original**: इस प्रकार आदि आप्नेय महाएटाणमें 'प्मीके व्रतोंका वर्णन” नामक एक साौँ इक्यासीयाँ अध्याय पूरा हुआ
- **Translation**: 

---

### Verse 18 (Agni Puran 0.3598)
- **Original**: 8 0 एक सौ बयासीवाँ अध्याय सप्तमी तिथिके ब्रत अग्निदेव कहते हैं-- वसिष्ठ ! अब मैं सप्तमी
- **Translation**: 

---

### Verse 19 (Agni Puran 0.3599)
- **Original**: निराहार रहकर सूर्यदेवका पूजन करनेसे सारे तिथिके व्रत कहूँगा। यह सबको भोग और मोक्ष
- **Translation**: 

---

### Verse 20 (Agni Puran 0.3600)
- **Original**: पापोंका विनाश होता है
- **Translation**: 

---

