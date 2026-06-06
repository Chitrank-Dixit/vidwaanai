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

### Verse 1 (Vishnu Puran 0.9641)
- **Original**: जो व्यक्ति जिस चिद्यासे युक्त हैं उसकी वही इशष्टदेवता है, वहीं पूजा-अर्चाके योग्य है और यही परम उपकारिणी है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9642)
- **Original**: जो पुरुष एक व्यक्तिसे फल्-स्म्रथध करके अन्यक्ी पूजा करता है उसका इहलेक अथवा परलोकसें कहां भो शुभ नहीं होता
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9643)
- **Original**: खेतोंकि अन्तमें सीमा है तथा सीमाके अन्तमें बन हैं और बनोंके अन्तमें समस्त पर्वत हैं; वे पर्वत ही हमारी परमगति हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9644)
- **Original**: इमलोग न तो किंवाड़ें तथा भितिके अच्दर रहनेबाले हैं और न निश्चित गृह अथवा खेतवाले किसान हो हैं, बल्कि [ बन-पर्वतादिमें स्वच्छन्द बिचरनेवाले ] हमलोग चक्रचारी” मुनियोंकी भाँति समस्त जनसमुदायमें सुख्यी हैं (अतः गृहस्थ किसानॉकी भाँति हमें इन्द्रकी पूजा करनेका क्येई काम नहों]'”
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9645)
- **Original**: “सुना जाता है कि इस बनके पर्वतगण कामरूपी + चअक्रचारी मुनि ये हैं जो राकट आदिसे सर्वत्र भ्रमण किया कस्ते हैं और जिनका कोई सास निवास कहीं होता । जहाँ जाम हो जाती है वहीं रह जाते हैं। अतः उन्हें 'सायेगृह' मो कहते हैं ।
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9646)
- **Original**: के38 यदा चेतै: प्रब्ााध्यन्ते तेघां ये काननौकस: । तदा सिंहादिरूपैस्तान्धातयन्ति महीधरा:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9647)
- **Original**: 35 गिरियज्ञस्त्वय॑तस्माद्रोयज़श् प्रवर्त्यताम्‌। किमस्माक॑ महेन्द्रेण गावइझैलाओ देवता:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9648)
- **Original**: 36 मन्त्रज्ञपरा विप्रास्सीरयज्ञाश्ष कर्षका: । गिरिगोयज्ञशीलाश्षन॒ वयमद्रिवनाश्रया:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9649)
- **Original**: 37 तस्माद्वेवर्धनइशैलो भवद्धिर्बिविधाईणै: । अर्च्यतां पूज्यतां मेथ्यान्पशून्हत्वा विधानतः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9650)
- **Original**: 38 सर्वघोषस्य सन्‍्दोहो गृह्मातां मा विचार्यताम्‌ । भोज्यन्तां तेन वै विप्रास्तथा ये चाभिवाउछका:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9651)
- **Original**: 39 तत्रार्चिते कृते होमे भोजितेषु द्विजातिषु । शरत्पुष्पकृतापीडा: परिगच्छन्तु गोगणा:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9652)
- **Original**: 40 एतन्पम मरते गोपास्सम्प्रीत्या क्रियते यदि । ततः कृता भवेत्मीतिर्गवामद्रेस्तथा मम
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9653)
- **Original**: 49 श्रीपपाशर उबाय इति तस्य बच: श्रुत्वा नन्‍्दाद्मास्ते ब्रजोकस: । प्रीत्युत्फुल्लमुखा गोपास्साधुसाध्वित्यथान्ुवन्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9654)
- **Original**: 42 शोभनं ते मतं वत्स यदेतद्भवतोदितम्‌। तत्करिष्यामहे सर्व गिरियज्ञ: प्रवर्त्सताम
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9655)
- **Original**: 43 तथा च कृतवन्तस्ते गिरियज्ञं ब्रजौकसः: । द्धिपायसमांस्;ोर्ददुश्शैलबलिं..._ ततः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9656)
- **Original**: 'डड द्विजांश्व भोजयामासुश्शतशो5थ सहस्नञ्म:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9657)
- **Original**: 45 गाबइश्ैलं ततश्नक्ररचिंतास्ता: प्रदक्षिणम। वृषभाश्चातिनर्टनन्‍्तस्सतोया जलदा डइब
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9658)
- **Original**: 46 गिरिमूर्द्धने कृष्णो5पि शैलो5हमिति मूर्तिमान्‌ । बुभुजेउन्न॑ बहुतरं गोपवर्याहत॑द्विज
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9659)
- **Original**: 47 स्वेनैव कृष्णो रूपेण गोपैस्सह गिरेहिद्वार: । अधिरुह्वार्चयामास द्वितीयामात्पनस्तनुप्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9660)
- **Original**: 48 अन्तर्द्धन गते तस्पिन्गोपा लब॒ध्वा ततो बरान्‌ । कृत्वा गिरिमख॑ गोष्ठ॑ निजमभ्याययु: पुनः
- **Translation**: 

---

