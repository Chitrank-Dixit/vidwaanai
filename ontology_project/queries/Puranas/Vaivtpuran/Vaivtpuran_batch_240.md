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

### Verse 1 (Vaivtpuran 13.10942)
- **Original**: मुनिना कोर्तिता तेने शरच्चन्द्रप्रभानना
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10943)
- **Original**: ड्दं घोड़शनामोक्तमर्थव्याख्यानसंयुतम्‌ । नारायणेन. यद्दत्त ब्रह्मणे.. नाभिपड्रूजे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10944)
- **Original**: ब्रह्मणा च पुरा दत्त धर्माय जनकाय में
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10945)
- **Original**: धर्मेणम कृपया दत्त महामादित्यपर्वणि
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10946)
- **Original**: ड्ट8ट * संक्षिप्त ग्रह्मवैवर्तपुराण + $%$%%%%%######## # #%%%ऊ कक %&#####%$%$%ऋ%## # ###### कक # कक ककककऊकश़्ऋऊऋड़कककक़ नारदजीने कहा--प्रभों! यह सर्वदुर्लभ
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10947)
- **Original**: तिरोभूत होता रहता है, उनके लिये क्या और परम आश्चर्यमय स्तोत्र मुझे प्राप्त हुआ। देवी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10948)
- **Original**: कैसे असाध्य है? अहो! जिनके रोमकूपोंमें ही श्रीराधाका “संसारविजय' नामक कवच भी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10949)
- **Original**: सारे ब्रह्माण्ड स्थित हैं, उन परमेश्वर महाविष्णु उपलब्ध हुआ। सुयज्ञने जिसका प्रयोग किया
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10950)
- **Original**: श्रीहरिके लिये क्या असाध्य हो सकता है ? ब्रह्मा, था, वह दुर्लभ स्तोत्र भी मुझे सुलभ हो गया।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10951)
- **Original**: शेषनाग, शिव और धर्म जिनके चरणारविन्दोंका भगवान्‌ श्रीकृष्णकी विचित्र कथा सुनकर
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10952)
- **Original**: दर्शन करते रहते हैं, उन माया-मानव-रूपधारी आपके चरणकमलोंके प्रसादसे मैंने बहुत
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10953)
- **Original**: परमेश्वके लिये कौन-सा ऐसा कार्य है, जो कुछ पा लिया। अब मैं जिस रहस्यको
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10954)
- **Original**: असाध्य हो ?' नन्दजीने उस नगरमें घूम-घूमकर, सुनना चाहता हूँ, उसका वर्णन कीजिये। मुने
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10955)
- **Original**: एक-एक घरको देख-देखकर और वहाँ लिखे वृन्दावनमें प्राः:काल उस अद्भुत नगरको
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10956)
- **Original**: हुए नामोंकों पढ़कर सबके लिये घरोंका वितरण देखकर गोपोंने क्या कहा? किया। नन्‍्द और वृषभानुने शुभ मुहूर्त देखकर भगवान्‌ श्रीनारायण बोले--नारद! जब
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10957)
- **Original**: प्रवेशकालिक मड्भनलकृत्यका सम्पादन करके वहाँ रात बीत गयी, विश्वकर्मा चले गये और
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10958)
- **Original**: अपने सेवकगणोंके साथ अपने-अपने आश्रममें अरुणोदयकी बेला आयी, तब सब लोग जाग
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10959)
- **Original**: प्रवेश किया। वृन्दावनमें रहकर उन सबके मुख उठे। उठते ही सबसे बिलक्षण उस नगरको देख और नेत्र प्रसन्नतासे खिल उठे। उन सब गोपोंने भ्रजवासी आपसमें कहने लगे-'यह क्‍या श बड़े आनन्दके साथ अपने-अपने उत्तम आश्रममें है? यह क्या आश्चर्य है?' किन्हीं गोपोने कुछ पदार्पण किया। अपने-अपने मनोहर स्थानपर अन्य गोपोंसे पूछा-“यह कैसे सम्भव हुआ ?
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10960)
- **Original**: सब गोपोंको बड़ा आनन्द मिला। वहाँके बालक न जाने भूतलपर किस रूपसे कौन प्रकट हो
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10961)
- **Original**: और बालिकाएँ हर्षपूर्वक खेलने-कूदने लगीं। सकता है?' परंतु नन्दरायजी गर्गके वाक्योंका
- **Translation**: 

---

