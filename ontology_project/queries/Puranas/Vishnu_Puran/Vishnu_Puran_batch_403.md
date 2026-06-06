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

### Verse 1 (Vishnu Puran 0.8041)
- **Original**: उसके धर्म, वायु और इन्द्रके द्वारा क्रमशः युधिप्ठिर, भीमसेन और अर्जुन नामक तोन पुत्र हुए
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8042)
- **Original**: इनके पहले इसके अविवाहिताबवस्थामें ही भगवान्‌ सूर्यके द्वार कर्ण नामक एक कानीनाँ पुत्र और हुआ था
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8043)
- **Original**: इसकी माद्री नामकी एक सपल्नी थी
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8044)
- **Original**: उसके अशिनीकुमारोंद्वारा नकुछ और सहदेव नामक पाण्डके दो पुत्र हुए
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8045)
- **Original**: शुरसेनकी दूसरी कत्या श्रुतदेवाका कारूडा-नरेश वृद्धधर्मासे विवाह हुआ था
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8046)
- **Original**: उससे दन्तबक्र नामक महादैत्य उत्पन्न हुआ
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8047)
- **Original**: श्रुतकीर्तिको केकयराजने विवाहा था
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8048)
- **Original**: उससे केकय-नरेदके सन्‍्तर्दन आदि पाँच पुत्र हुए
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8049)
- **Original**: राजाधिदेवीसे अवत्तिदेशीय विन्द और अनुविन्दकां जन्म हुआ
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8050)
- **Original**: अुतश्रणाका भी चेदिराज दमघोषने पाणिग्रहण किया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8051)
- **Original**: उससे दिशुपालका जन्म हुआ
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8052)
- **Original**: पूर्वजन्ममें यह अतिशय पयक्रमी हिरण्यकशिपु. नामक दैत्योंका मूल पुरुष हुआ था जिसे सकल -लोकगुरु + अवियाहिता कन्याके गर्धसे हुए पुत्रको क्य्नीन कहते हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8053)
- **Original**: आन 15 ] यश्ञ॒भगवता सकललोकगुरुणा नरसिंहेन घातित:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8054)
- **Original**: पुनरपि अक्षयवीर्यशौर्यसम्प त्पराक्रमगुणस्समाक्रान्तसकलत्रैल्लेक्येश्वरप्रभावो द्शाननो नामाभूत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8055)
- **Original**: बहुकाल्परेपभुक्त भगवत्सकाशाबाप्तझरीरपातोद्धवपुण्यफलो भगवता राघवरूपिणा सो5पि निधनमुप- पादित:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8056)
- **Original**: पुनश्चेदिराजस्य दमघोषस्यात्मज- हिशज्ुपालनामाभवत्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8057)
- **Original**: शिकशुपाल त्वेषप भगवतो भूभारावतारणायावतीर्णांशस्य पुण्डरीकनयनाख्यस्योपरि ब्वेषानुबन्धमतित- राजक्षकार
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8058)
- **Original**: भगवता च स निधनमुपनी- तस्तत्रैव परमात्मभूते मनस एकापग्रतया सायुज्य- मवाप
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8059)
- **Original**: 52 । भगवान्‌ यदि प्रसन्नो यथाभिलपितं ददाति तथा अप्रसन्नो5पि निप्नन्‌ स्थान॑ प्रवच्छति
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8060)
- **Original**: चतुर्थ अंदा 283 भगवान्‌ नृसिहने मारा था
- **Translation**: 

---

