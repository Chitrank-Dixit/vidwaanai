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

### Verse 1 (Vaivtpuran 21.18762)
- **Original**: बेदा न शक्ता नो बाणी नच लक्ष्मी: सरस्वती । न राधा स्तबने शक्ता कि स्तुबन्ति विपश्चित:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 21.18763)
- **Original**: क्षमस्तव निखिल ब्रह्मन्नपरार्थ क्षणे क्षणे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 21.18764)
- **Original**: रक्ष मां करुणासिन्धो दीनबन्धो भवार्णवे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 21.18765)
- **Original**: पुरा तीर्थ तपस्तप्त्वा पुत्र: प्राप्त: सनातन: । स्वकीयचरणापम्भोजे भक्ति दास्यं च देहि मे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 21.18766)
- **Original**: * अश्रीकृष्णस्तोत्राणि + <रेर 25 %%%#64#%4%6####### %# 41% $%$ 55% $% $% 55% %%%% 5 ऋकऋ%ऊऋऊऋऊऋऋऋऋछ% %%%%%कऋ कक % 55% ऋ%क% $ डरहात्वममरत्य॑ वा सालोक्यादिकमेव वा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 21.18767)
- **Original**: त्वत्पदाम्भोजदास्यस्थ कलां नाईन्ति घोडशीम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 21.18768)
- **Original**: इन्द्रत्व॑ वा सुरत्व॑ वा सम्प्राप्तिं सिद्धरिस्वर्गयों: । राजत्व॑ चिरजीवित्व॑ सुधियो गंणयन्ति किम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 21.18769)
- **Original**: एतद्‌ यत्‌ कथितं सर्य ब्रह्मत्यादिकमीश्वर । भक्तसड्डक्षणार्धल्य नोपमभा ते किमईति
- **Translation**: 

---

### Verse 9 (Vaivtpuran 21.18770)
- **Original**: त्वदूभक्तो यस्त्वत्सदृशः कस्त्वां तर्कितुमीश्चरः
- **Translation**: 

---

### Verse 10 (Vaivtpuran 21.18771)
- **Original**: क्षणार्थालापमात्रेण पार कर्तु स॒चेश्वर:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 21.18772)
- **Original**: भक्तसड्राद्‌_ भवत्येव भक्त्यद्वुरमनेकधां । त्वदूभक्तजलदालापजलसेकेन वर्धते
- **Translation**: 

---

### Verse 12 (Vaivtpuran 21.18773)
- **Original**: अभक्तालापतापात्तु शुष्कतां याति तत्क्षणम्‌ । तदगुणस्मृतिसेकाच्य बर्धते तत्क्षणे स्फुटम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 21.18774)
- **Original**: त्वद्धक्त्यद्शुरमुदभूत॑ स्फीतं ' मानसज॑ परम्‌ । न नश्यं वर्धनीयं च॒ नित्य॑ नित्यं क्षणे क्षणे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 21.18775)
- **Original**: ततः सम्प्राप्य म्रह्मत्व॑ भक्तस्य जीवनाय च॑ । ददात्वेव फलं तसस्‍्म हरिदास्यमनुत्तमम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 21.18776)
- **Original**: संप्राप्य दुर्लभ॑ दास्यं यदि दासो बभूब ह । सुनिश्चययेन. तेनेव जित॑ सर्व॑ भयादिकम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 21.18777)
- **Original**: इत्येबमुक्त्था भकत्या च नन्दस्तस्थौ हरे: पुर: । प्रसन्नचदनः कृष्णों ददौ तस्मै तदीप्सितम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 21.18778)
- **Original**: एवं नन्दकृत॑ स्तोत्र नित्य भक्‍त्या च यः पठेतू । सुदृढां भक्तिमाप्रोति सद्यो दास्‍्य॑ लभेद्धरे:
- **Translation**: 

---

### Verse 18 (Vaivtpuran 21.18779)
- **Original**: ड्ति श्रीब्रह्मवैवर्ते तन्दकृत॑ श्रीकृष्णस्तवन सम्पूर्णप्‌ । ( श्रीकृष्णजन्मखण्ड 21। 200--223) धेनुकभीतैगोंपबालकै: कृतं श्रीकृष्णस्तवनम्‌ त॑ दृष्टा रुरुदुः सर्वे फलानि तत्यजुर्भिया। कृष्ण कृष्णेति शब्दं च॒ प्रचक्रुर्जदुधा भृशम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 21.18780)
- **Original**: अस्मान्‌ रक्ष समागच्छ हे कृष्ण करुणानिधे। हे संकर्षण नो रक्ष प्राणा नो यान्ति दानवात्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 21.18781)
- **Original**: है कृष्ण हे कृष्ण हरे मुरारे गोविन्द दामोदर दीनबन्धो। गोपीश गोपेश भवार्णवेउस्माननन्त नारायण रक्ष रक्ष
- **Translation**: 

---

