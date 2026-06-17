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

### Verse 1 (Ling 0.461)
- **Original**: . तत्पुरुषाय विद्महे वक्रतुण्डाय श्रीमहि तन्नो दकत्तिः प्रचोदयात्‌
- **Translation**: 

---

### Verse 2 (Ling 0.462)
- **Original**: क श्री लिंग पुराण क 379 महासेनाय विदमहे वाग्विशुद्धाय धीमहि तन्नः स्कन्दः प्रचोदयात्‌
- **Translation**: 

---

### Verse 3 (Ling 0.463)
- **Original**: तीक्ष्ण श्रूद्धाय विद्महे बेदपादाय धीमहि तन्नो वृषः प्रचोदयात्‌
- **Translation**: 

---

### Verse 4 (Ling 0.464)
- **Original**: हरिवक्त्राय विदमहे रुद्रवक्त्राय धीमहि तन्नो नन्दी प्रचोदयात्‌
- **Translation**: 

---

### Verse 5 (Ling 0.465)
- **Original**: नारायणाय विदमहे वासुदेवाय धीमहि तन्नो विष्णु प्रचोदयात्‌
- **Translation**: 

---

### Verse 6 (Ling 0.466)
- **Original**: महाम्भिकायै विद्महे कर्म्मसिद्धै च धीमहि तन्नो लक्ष्मी: प्रचोदयात्‌
- **Translation**: 

---

### Verse 7 (Ling 0.467)
- **Original**: समुद्धृताये॑विदमहे विष्णुनैकेन धीमहि तन्नो राधा प्रचोदयात्‌
- **Translation**: 

---

### Verse 8 (Ling 0.468)
- **Original**: बवैनतेयाय विद्महे सुवर्णपक्षाय धीमहि तन्नो गरुड़ः प्रचोदयात्‌
- **Translation**: 

---

### Verse 9 (Ling 0.469)
- **Original**: शिवास्यजायै विद्महे देवरूपायै थीमहि तन्नो वाचा प्रचोदयात्‌
- **Translation**: 

---

### Verse 10 (Ling 0.470)
- **Original**: पदमोद्रभवाय विदमहे बेदवक्त्राय थीमहि तन्नो सृष्टा प्रचोदयात्‌
- **Translation**: 

---

### Verse 11 (Ling 0.471)
- **Original**: शिवास्यजायैविद्महे देवरूपायै धीमहि त्न्नो वा प्रचोदयात्‌
- **Translation**: 

---

### Verse 12 (Ling 0.472)
- **Original**: देवराजाय विदमहे वज्रहस्ताय धीमहि तन्नः शंक्रः प्रचोदयात्‌
- **Translation**: 

---

### Verse 13 (Ling 0.473)
- **Original**: 380 क श्री लिंग पुराण # रुद्रनेत्राय विद्महे शक्ति हस्ताय धीमहि तन्नो वह्नि प्रचोदयात्‌
- **Translation**: 

---

### Verse 14 (Ling 0.474)
- **Original**: वैवस्वताय विद्महे दण्ड हस्ताय धीमहि तन्नो यमः प्रचोदयात्‌
- **Translation**: 

---

### Verse 15 (Ling 0.475)
- **Original**: निशाचराय विदमहे खड्गहस्ताय धीमहि तन्नो निऋतिः प्रचोदयात्‌
- **Translation**: 

---

### Verse 16 (Ling 0.476)
- **Original**: शुद्धहस्ताय विद्महे पाशहस्ताय धीमहि तत्नो वंरुणः प्रचोदयात्‌
- **Translation**: 

---

### Verse 17 (Ling 0.477)
- **Original**: सर्वप्राणाय विद्महे यष्टि हस्ताय धीमहि तन्नो वायु: प्रचोदयात्‌
- **Translation**: 

---

### Verse 18 (Ling 0.478)
- **Original**: यक्षेश्वराय विदमहे गदाहस्ताय थीमहि ततन्नो यक्षः प्रचोदयात्‌
- **Translation**: 

---

### Verse 19 (Ling 0.479)
- **Original**: कात्यायन्यै विद्महे कन्य ( नया ) कुर्भाय धीमहि तन्नो दुर्गा प्रचोदयात्‌
- **Translation**: 

---

### Verse 20 (Ling 0.480)
- **Original**: इस प्रकार से तत्‌ तत्‌ देव के अनुरूप भिन्न भिन्न गायत्री से देवताओं की पूजा और स्थापना करनी चाहिए अथवा अतुल विष्णु भगवान को पुरुष सूक्त से या देव गायत्री से स्थापना करनी चाहिए। वासुदेव प्रथान है, फिर वे शंकरषण हैं, फिर प्रद्युम्न हैं, ये उनके मूर्ति के भेद हैं। बहुत प्रकार की भगवान की शाप उत्पन्न मूर्ति जगत के हित के लिए हैं जैसे मत्स्य, कूर्म, वराह, नरसिंह, वामन, राम, कृष्ण, बौद्ध, कल्कि तथा अन्य भी भगवान
- **Translation**: 

---

