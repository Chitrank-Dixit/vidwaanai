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

### Verse 1 (Markende Puran 0.3161)
- **Original**: #न्जटरिकप4:2क्‍02-
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3162)
- **Original**: #निशुम्भ-चप्च +
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3163)
- **Original**: 4070714045346.64464444 » 50 » 05 21 5344
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3164)
- **Original**: 446544 8544 70मशजकशंशअ 35:544:0:606 6 /#4400007 ह 33.48 )6/6.4.65/6/0/:0/ र्र्3 नवमो5ध्यायः निशुम्भ-वध घ्यान ( &0 बन्धूककाझननिभे रुचिराक्षपालां पाशाद्लुशौ च वरदां निजयाहुदण्डैः। विभ्राणम्न्दुशकलाभरणं जिलेत्र- प्रधाम्बिकैशमनिशं. वपुराश्रयात्रि
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3165)
- **Original**: मैं अर्थतारीभ्वरके श्रीबिग्रहकी निरन्तर शरण लेता हूँ। उसका वर्ण बम्धृकपुष्प और सुवर्णके समान रक्त-पीतपिश्रित है। बह अप्रनो भुजाओंमें सुन्दर अक्षमाला, पाश, अक्लुश और बरद-मुद्रा धारण करता है; अर्धचन्द्र उसका आभूषण है तथा नह तीन नेन्रोंसे सुशोभित हैं।) एजोकान / £
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3166)
- **Original**: '39'बिन्रित्रभिदमारघ्यातं भगवन्‌ भव्ता मघ। देव्याश्षर्तिमाहात्म्य॑ रक्तर्बीजवशाभशितम्‌
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3167)
- **Original**: भूयशछ्षेच्छाम्यहै आऔर्तु_रक्तबीजे निफ्रातिते। चकयर शुप्थों यत्कर्म निशुम्भभ्ञातिकोपयः
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3168)
- **Original**: जाने कहा--
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3169)
- **Original**: भगवन्‌। आपके रफ़तेबीजके वथसे सम्बन्ध रखनेबाला देवी-चरित्रका यह अद्भुत माहात्म्य मुझे बतलाया
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3170)
- **Original**: अगर रक्बीजके मारे जानेपर अत्यन्त क्रोभ्पें भरे हुए शुष्प और निशुम्भने जो कर्य किया, उप्तकों में सुनना चाहता हूँ
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3171)
- **Original**: फऋषिरुबाच
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3172)
- **Original**: 44 अकार कोपमतुल॑ रक्तनीजे निषातिते। शुप्भासुरों निशुध्भक्ष हत्तेष्लन्थेषु चाहये
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3173)
- **Original**: इन्यमान॑ महासैन्य॑ विलोक्यापर्पमुद्दहन्‌। अभ्यधावत्रिशुम्भोड्थ मुख्यबासुरसेनया
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3174)
- **Original**: जस्याग्रत॒स्तथ्ा पृष्ठे प्रार्थयोश्ष महासुरा।। 1. पा0--3$5शु शरोत्करे: । 2. पा2--आयान्तं। 3 संदष्ट्रीएपुटा: क्रुद्धा हन्तुं देवीमुपाययु: ध'9
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3175)
- **Original**: आजगाम महावीर्य; शुम्भोजपि स्वबलैर्ृत:। निहन्तुं चण्डिकां कोपात्कृत्ता युद्ध तु मातृभि:
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3176)
- **Original**: त़तों युख्भपतीबासीद्वेव्या शुम्भनिशुध्भयो:। शरवर्षमतीयोग्र. मेघयोरिव वर्षतो:
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3177)
- **Original**: 9 चिच्छेदास्ताययंस्ताभ्वां चण्डिका स्वशसेत्क:9। ताडयाघास॒ चाह्लेंघ शस्त्रौधैरसुरेक्षरौ
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3178)
- **Original**: निशुम्भो निश्ितं खड्गं चर्म चादाय सुप्रभम्‌। अताडयन्पूर्शि सिंहे देव्या वाहनमुन्तमप्‌
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3179)
- **Original**: ताहिते वाइने देवी क्षुरप्रेणासिपुत्तमम्‌! निशुम्भस्याशु चिच्छेद चर्म चाप्यष्टचद्धकम्‌ 422
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3180)
- **Original**: 'ठिब्रे चर्मणि सड़्गे च शक्ति चिक्षेप सोडसुद । तामप्यस्थ द्विधा चक्रे चक्रेणाभिमुस्यागताम्‌
- **Translation**: 

---

