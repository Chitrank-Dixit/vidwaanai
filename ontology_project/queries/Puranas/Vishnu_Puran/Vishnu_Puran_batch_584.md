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

### Verse 1 (Vishnu Puran 0.11661)
- **Original**: उग्रसेनने उस लोहमय मूसरूका चूर्ण करा डाल्म और उसे उन बालकोंने [ले जाकर] समुद्रमें फेंक दिया, उससे वहाँ यहुत-से सरकण्डे उत्पन्न हो गये
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11662)
- **Original**: यादलॉंद्वारा चूर्ण किये गये इस मूसलके लोहेका जो भालेकी नॉकके समान एक खण्ड चूर्ण करनेसे बचा उसे भी समुद्रहीमें फिकवा दिया। उसे एक मछली निगल गयी। उस मछलीको मछेरोंने पकड़ लिया तथा चौरनेपर उसके पेटसे निकले हुए उस सूसलखण्डको जरा नामक व्याधने ले लिया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11663)
- **Original**: भगवान्‌ मधुसूदन इन समस्त बातोंको यथावत्‌ जानते थे तथापि उन्होंने बिधाताकी इच्छाकों अन्यथा करना न चाहा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11664)
- **Original**: इसी समय देवताओनि वायुकों भेजा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11665)
- **Original**: उसने एक्य्रन्तमें श्रीकृष्णचन्द्रको प्रणाम करके कहा--''भगवन्‌ ! मुझे देवबताओंने दूत बनाकर भेजा है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11666)
- **Original**: “हे बिभो ! वसुगण, अश्विनीकुमार, रुद्र, आदित्य, मरुद्ण' और साध्यादिके सहित इन्द्रने आपको जो सन्देश भेजा है वह
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11667)
- **Original**: आः 37 । भारावतरणार्थाय वर्षाणामधिक॑ शतम्‌ । भगवानवतीर्णोउत्र त्रिदवैस्सह चोदित)
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11668)
- **Original**: 18 दुर्वृत्ता निहता दैत्या भुबो भारोउवतारित: । त्वया सनाथास्तरिदशा भवन्तु त्रिदिवे सदा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11669)
- **Original**: 19 तदतीत॑ जगन्नाथ वर्षाणामधिक शत्तम्‌। दुदानीं गम्यतां स्वर्गों भवता यदि रोचते
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11670)
- **Original**: 20 देवैर्विज्ञाप्पते देव तथात्रैब रतिस्तव । तत्स्थीयतां यथाकालमाख्येयमनुजीविधभि:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11671)
- **Original**: 21 यक्त्वमात्थास्विलं दूत वेद्म्वेतदहमप्युत । प्रारव्ध एवं हि मया यादव्मनां परिक्षयः
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11672)
- **Original**: 22 भुवो नाद्यापि भारो5यं यादवैरनिबर्हितैः । अबतार्य करोम्येतत्सप्तरात्रेण सत्बरः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11673)
- **Original**: 23 यथा गृहीतामम्भोधेर्दत्त्वाह॑ द्वारकाभुवम्‌ । यादवानुपसंहत्य यास्यापि तब्रिदशालयम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11674)
- **Original**: 24 मनुष्यदेहमृत्सुज्य. सह्डूर्षणसहायवान्‌ । प्राप्त एवाप्मि मन्तव्यो देवेन्द्रेण तथामरैः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11675)
- **Original**: 27 जरासआआादयो येउन्ये निहता भारहेतवः । क्षितेस्तेभ्यः कुमारो5पि यदूनां नापत्नीयते
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11676)
- **Original**: 26 तदेते॑ सुमहाभारमवतार्य. क्षितेरहम्‌। यास्थाष्यमरलोकस्य पाल्कनाय ब्रवीहि तान्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11677)
- **Original**: 27 श्रीपशाशर उवाच इत्युक्तो बरासुदेवेन देवदूत: प्रणम्य तम्‌। पैत्रेय दिव्यया गत्या देवराजान्तिकं ययौ
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11678)
- **Original**: 28 भगवानप्यथो त्पातान्दिव्यभौमान्तरिक्षजान्‌ । दर्दर्श द्वारकापुर्याँ विनाशाय दिवानिश्ञप्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11679)
- **Original**: 29 तान्दृूद्ठा यादवानाह पश्यथ्वमतिदारुणान्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11680)
- **Original**: महोत्पाताज्व्छमायैषां प्रभासं याम मा चिरम्‌
- **Translation**: 

---

