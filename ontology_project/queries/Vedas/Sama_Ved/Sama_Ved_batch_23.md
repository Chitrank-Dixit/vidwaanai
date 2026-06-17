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

### Verse 1 (Sama Ved 0.441)
- **Original**: इन्द्रदेव की प्रशंसा करने वाले याज्ञिकगण अपनी शवित से हमारे यज्ञ में अवभूथ स्नात (यज्ञ की समाप्ति पर होने वाला स्नान) होने तक यज्ञाहुतियाँ देते हैं
- **Translation**: 

---

### Verse 2 (Sama Ved 0.442)
- **Original**: पूर्वार्थिक ऐडपर्वाण ट्वितोयो5 ध्याय: 2.5 152. अहमिद्धि पितुष्परि मेधामृतस्य जग्रह। अहं सूर्य इवाजनि
- **Translation**: 

---

### Verse 3 (Sama Ved 0.443)
- **Original**: हमने (याजक) पालनकर्ता यज्ञरूपी इन्द्रदेव की बुद्धि को अपनी ओर आकर्षित कर लिया है । इससे हम सूय्यदेव के सदृश तेज से युक्त हो गये हैं
- **Translation**: 

---

### Verse 4 (Sama Ved 0.444)
- **Original**: 153. रेयतीर्न: सधमाद इन्द्रे सन्‍्तु तुविवाजा:। क्षुमन्तो याभिर्मदेम
- **Translation**: 

---

### Verse 5 (Sama Ved 0.445)
- **Original**: जिन (इन्द्र) की सहायता से हम धन-धान्य से परिपूर्ण होकर प्रफुल्लित होते हैं, उन इन्द्रदेव के प्रभाव से युक्त होकर हमारी गौएँ दुग्धादि देकर हमें अधिक सामर्थ्य देने वाली बन जाती हैं
- **Translation**: 

---

### Verse 6 (Sama Ved 0.446)
- **Original**: 154.सोम: पृषा च चेततुर्विश्वासां सुक्षितीनाम्‌। देवत्रा रथ्योर्हिता
- **Translation**: 

---

### Verse 7 (Sama Ved 0.447)
- **Original**: देवताओं के रथ में आसीन सोम और पूषादेव मनुष्यमात्र को स्फूर्ति देने वाले हैं
- **Translation**: 

---

### Verse 8 (Sama Ved 0.448)
- **Original**: डइ्ति चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.449)
- **Original**: हे ऋे के
- **Translation**: 

---

### Verse 10 (Sama Ved 0.450)
- **Original**: पश्चञम: खण्ड:
- **Translation**: 

---

### Verse 11 (Sama Ved 0.451)
- **Original**: 155. पान्तमा यो अन्धस इन्द्रमभि प्र गायत । विश्वासाहं शतक्तु मंहिष्ठं चर्षणीनाम्‌
- **Translation**: 

---

### Verse 12 (Sama Ved 0.452)
- **Original**: हे याजको ! सामर्थ्यवान्‌ सैकड़ों प्रकार के कर्म करने वाले, शत्रुनाशक सोमपायी इन्द्रदेव की विशेष स्तुतियों से प्रार्था करो ।1
- **Translation**: 

---

### Verse 13 (Sama Ved 0.453)
- **Original**: 156. प्र व इन्द्राय भादन॑ हर्यश्राय गायत। सखाय: सोमपाव्ने
- **Translation**: 

---

### Verse 14 (Sama Ved 0.454)
- **Original**: है साधको ! किरणरूपी घोड़ों के स्वामी, सोमपायी इन्द्र को आनन्द प्रदान करने वाले स्तोत्रों का गान करो
- **Translation**: 

---

### Verse 15 (Sama Ved 0.455)
- **Original**: 157, वयमु त्वा तदिदर्था इन्द्र त्वायन्त: सखाय: । कण्वा उक्थेभिर्जरन्ते
- **Translation**: 

---

### Verse 16 (Sama Ved 0.456)
- **Original**: हे इन्रदेव ! आपसे मित्रता करने के इच्छुक, आपके सखा हम, आपके स्तोता तथा सभी कण्व-वंशो, स्तुतियों द्वारा आपकी प्रशंसा करते हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.457)
- **Original**: 158. इन्द्राय मद्दने सुतं परि ष्टोभन्तु नो गिर: । अर्कमर्चन्तु कारव:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.458)
- **Original**: आनन्दमयी प्रकृति वाले इन्द्रदेव के निमित्त निकाले गये दिव्य सोमरस की, हम वाणी द्वारा प्रशंसा करें । स्तोतागण, इस पूज्य सोम की प्रार्थना करें
- **Translation**: 

---

### Verse 19 (Sama Ved 0.459)
- **Original**: 159, अयं त इन्द्र सोमो निपूतो अधि बर्हिंषि
- **Translation**: 

---

### Verse 20 (Sama Ved 0.460)
- **Original**: एहीमस्य द्रवा पिब
- **Translation**: 

---

