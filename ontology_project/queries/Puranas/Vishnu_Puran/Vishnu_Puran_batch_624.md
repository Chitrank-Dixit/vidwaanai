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

### Verse 1 (Vishnu Puran 0.12461)
- **Original**: प्रथम यम-किल्कुर अपने पाशॉमें बाँधते हैं; फिर उनके दण्ड-प्रहार सहने पढ़ते हैं, तदनन्तर यमराजका दर्शन होता है और वहाँतक पहुँचनेमें बड़ा दुर्गम मार्ग देखना पड़ता है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12462)
- **Original**: अश्रीविष्णुपुराण [ अब 7 । प्रत्येक नरके याश्व यातना द्विज दुःसहा:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12463)
- **Original**: 45 क्रकचैः पाठ्यमानानां मूषायों चापि दह्मताम्‌ । कुठारैः कृत्यमानानां भूमौ चापि निखन्यताम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12464)
- **Original**: 46 झूलेघ्वारोप्यमाणानां व्याप्रवक्‍त्रे प्रवेश्यताम्‌। गृप्नैस्सम्भक्ष्यमाणानां द्वीपिभिश्नोपभुज्यताम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12465)
- **Original**: 47 क्राथ्यतां तैलमध्ये च॒ छ्लिद्यतां क्षारकर्दमे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12466)
- **Original**: उच्चान्निपात्यमानानां क्षिप्यतां क्षेपवन्त्रकै:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12467)
- **Original**: 48 नरके यानि दुःखानि पापहेतूद्धवानि वै। प्राप्यन्ते नारकैर्जिप्र तेषां संख्या न विद्यते
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12468)
- **Original**: 49 न केवल द्विजश्रेष्ठ नरके दुःखपद्धति: । स्वगेंडपि पातभीतस्य क्षविष्णोर्नास्ति निर्वृतिः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12469)
- **Original**: 50 पुनश्च गर्भे भवति जायते च पुनः पुनः । गर्भे विलीयते भूयो जायमानो5स्तमेति वै
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12470)
- **Original**: 51 जातमात्रश्च प्रियते बालभावे5थ यौवने। मध्यमं वा वय: प्राप्य वार्डके वाथवा मृति:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12471)
- **Original**: 52 द्रव्यनाशे तथोत्पत्तौ पालने च सदा नृणाम्‌ भवकन्‍त्यनेकदुःखानि.. तथैवेष्टविपत्तिषु
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12472)
- **Original**: 54 यद्यत्रीतिकर पुंसां वस्तु मैत्रेय जायते। तदेव दुःखवृक्षस्यबीजत्वमुपगच्छति
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12473)
- **Original**: 55 कलच्पुत्रभित्रार्थगृहक्षेत्रधनादिकै: । क्रियते न तथा भूरि सुर्ख पुंसां यथाउसुखम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12474)
- **Original**: 56 इति संसारदुः:खार्कतापतापितच्ेतसाम्‌ । बिमुक्तिपादपच्छायामृते कुत्र सुर्ब॑ नृणाम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12475)
- **Original**: 57 तदस्य त्रिविधस्थापि दुःस्वजातस्य ये मम । गर्भजन्मजराद्येषु स्थानेषु॒प्रभविष्यतः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12476)
- **Original**: 58 निरस्तातिशयाह्वादसुखभावैकलक्षणा . । भेषज॑ भगवद्याप्तिरेकान्तात्यन्तिकी मता
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12477)
- **Original**: 59 तत्प्राप्निहेतुज्ञानं च कर्म चोक्ते महामुने
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12478)
- **Original**: 60 1-दह्यातामिल्यादिषु परस्मैपदमार्पम्‌ । हे द्विज! फिर तप्त बालुका, अग्नि-यत्ल और चास्थादिसे महाभयंकर नरकॉमें जो यातनाएँ भोगनी पड़ती हैं वे अत्यन्त असहा होती हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12479)
- **Original**: आरेसे चीरे जाने, मूसमें तपाये जाने, कुल्हाड़ीसे काटे जाने, भूमिमें गाड़े जाने, शूल्लीपर चढ़ाये जाने, सिंहके मुखमें डाले जाने, गिद्धोंके नोचने, हाथियोंसे दलित होने, तेलमें पकाये जाने, खारे दलूदलमें फैंसने, ऊपर ले जाकर नीचे गिराये जाने और क्षेपण-यन्त्नद्वारा दूर फेंके जानेसे नरकनिबासियोंकों अपने पाप-कर्मोके कारण जो-जो कष्ट उठाने पड़ते हैं उनकी गणना नहीं हो सकती
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12480)
- **Original**: 46---49
- **Translation**: 

---

