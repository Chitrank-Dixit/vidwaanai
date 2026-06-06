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

### Verse 1 (Vishnu Puran 0.2441)
- **Original**: हिरण्यकशिपु ओोला--यह दुर्बुद्धि बालक कोई ऐसी माया जानता है जिससे यह हमसे नहीं मारा जा सकता, इसलिये आप मायासे ही इसे मार हालिये
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2442)
- **Original**: झम्बरासुर खोल्ज--हे टैल्येन्द्र ! इस बालूकको में अभी मारे डालता हूँ, तुम मेरी मायाका नल देखो । देखो, मैं तुम्हें सैकड़ों-हजायें-करोड़ों मायाएँ दिखल्ाता हूँ
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2443)
- **Original**: श्रीपराझस्जी बोले--तबर उस दुर्दड्ध शाम्बरासुरने समदर्शीं प्रह्दांके लिये, उनके नाशकों
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2444)
- **Original**: <8 समाहितमतिर्भूत्वा शम्बरेषपि विमत्सर:। मैत्रेय सोउपि प्रह्मादः सस्मार मधुसूदनम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2445)
- **Original**: 18 ततो भगवता तस्थ रक्षार्थ चक्रपुत्तमम्‌। आजगाम समाज्ञप्त ज्वालामालि सुदर्शनम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2446)
- **Original**: 19 तेन मायासहस्न॑तत्छम्बरस्याशुगामिना । बालस्य रक्षता देहमेकेके च विश्ञोधितम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2447)
- **Original**: 20 संशोषक तथा वायु दैत्येन्द्रस्त्विदमब्रवीत्‌ । झीघ्रमेष ममादेशाहुरात्मा नीयतां क्षयम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2448)
- **Original**: 21 तथेत्युक्त्वा तु सोउप्येन॑ विवेश पवनो लघु । झीतो5तिरूक्ष: झोषाय तद्देहस्यातिदु:सह:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2449)
- **Original**: 22 तेनाविष्टमथात्मानं स युद्ध्वा दैत्यबालक: । हृदयेन महात्मान॑ दघार धरणीधरम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2450)
- **Original**: 23 इृदयस्थस्ततस्तस्थ ते वायुमतिभीषणम्‌ । पपोौ जनार्दन: क्रु्रः स ययो पवन: क्षयम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2451)
- **Original**: 24 क्षीणासु सर्वधायासु पवने सत्र क्षयं गते। जगाम सो5पि भवन गुरोरेव महामति:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2452)
- **Original**: 257 अहन्यहन्यथाचार्यों नीति राज्यफलप्रदाम्‌। ग्राहयामास त॑ बाल राज्ाघुझननसा कृताम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2453)
- **Original**: 26 गृहीतनीतिशास्त्रे ते बिनीते चर यदा गुरु: । मेने तदैन तत्पिश्रे कथयामास शिक्षितम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2454)
- **Original**: 27 आचार्य उवाच गृहीतनीतिझाख्स्ते पुत्रो दैत्यपते कृत: । प्र्भादस्तत्वतो वेत्ति भार्गवेण यदीरितम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2455)
- **Original**: 28 हिसण्यक्िएरवाच प्रह्माद त्रिषु लोकेषु मध्यस्थेषु कर्थ चरेत्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2456)
- **Original**: 29 कर्थ मन्त्रिपरमात्येषु बाह्नंप्लाभ्यन्तरेषु च। चारेषु पोरबर्गेषु शक्टितेश्चितरेष्‌ च
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2457)
- **Original**: 30 कृत्याकृत्यविधानश्न॒दुर्गाटविकसाधनम्‌ । च्रह्नाद कथ्यतां सम्यक्‌ तथा कण्टकशोधनम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2458)
- **Original**: 39 श्रीविष्णुपुराण ( आ0 19 इच्छासे बहुत-सी मायाएँ, रचीं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2459)
- **Original**: किन्तु, हे मैत्रेय ! शम्बरासुरके प्रति भी सर्वथा द्वेषहीन रहकर. प्रहादजी सावधान चित्तसे श्रीमघुसूदनभगवान्‌का स्मरण करते रहे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2460)
- **Original**: उस समय भगवान्‌की आज्ञासे उनकी रक्षाके लिये बहाँ ज्वाल्म-माल्जरओंसे युक्त सुदर्शनचक्त आ गया
- **Translation**: 

---

