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

### Verse 1 (Narsihma Puran 0.741)
- **Original**: 17--19
- **Translation**: 

---

### Verse 2 (Narsihma Puran 0.742)
- **Original**: थमी जोली--भैया! हम दोनों जुड़वी संतानें हैं और माताके गर्भमें एक साथ रहे हैं। पहले माताके
- **Translation**: 

---

### Verse 3 (Narsihma Puran 0.743)
- **Original**: र्भमें एक हो स्थानपर हम दोनोंका जो संयोग हुआ था, बह जैसे दूषित नहों माना गया, उसो प्रकार यह संयोग भी दूषित नहीं हो सफता। भाई ! अभोतक मुझे पतिको प्राप्ति नहीं हुई है। तूृम मेरा भला करना क्‍यों नहीं चाहते? 'निर्कतशि' सामक राक्षस तो अपनो बहितके साथ नित्य हो समागम करता है
- **Translation**: 

---

### Verse 4 (Narsihma Puran 0.744)
- **Original**: यम उकच स्ववम्भुवापि निन्‍्ोत लोकवृत्त जुगुप्सितम्‌। प्रधानपुरुषाचीर्ण लोको5यमनुबर्तते
- **Translation**: 

---

### Verse 5 (Narsihma Puran 0.745)
- **Original**: 22 तस्मादनिन्दितं धर्म प्रधानपुरुषक्षरेत्‌। निन्दितं वर्जयेद्यत्रादेतद्धर्मस्य लक्षणम्‌
- **Translation**: 

---

### Verse 6 (Narsihma Puran 0.746)
- **Original**: 23 यहायदाचरति .श्रेष्ठस्तत्तदेवेतरो. जनः। स॒ यत्प्रमाणं कुरुते लोकस्तदनुबर्तते
- **Translation**: 

---

### Verse 7 (Narsihma Puran 0.747)
- **Original**: 24 अतिपापमहं॑ मन्ये सुभगे बचने तब। विरुद्ध सर्वधर्मेंधू लोकेषु न विशेषतः
- **Translation**: 

---

### Verse 8 (Narsihma Puran 0.748)
- **Original**: 25 मत्तोउन्यों यो भवेद्यो वै विशिष्टो रूपशीलत:
- **Translation**: 

---

### Verse 9 (Narsihma Puran 0.749)
- **Original**: तेन सार्थ प्रमोदस्व न ते भर्ता भवाम्यहम्‌
- **Translation**: 

---

### Verse 10 (Narsihma Puran 0.750)
- **Original**: 26 नाह स्पृशामि तन्या ते तनुं भद्ने दृढब्नतः। मुनय: यापपमाहुस्तं यः: स्वसारं निगृद्धति
- **Translation**: 

---

### Verse 11 (Narsihma Puran 0.751)
- **Original**: 27 अम्युवाच दुर्लभ चैब पश्यामि लोके रूपमिहेदृशम्‌। यत्र रूप॑ बयश्चैव पृथिव्यां क्र प्रतिष्ठितम्‌
- **Translation**: 

---

### Verse 12 (Narsihma Puran 0.752)
- **Original**: 28 न बिजानामि ते चित्त कुत एतत्‌ प्रतिप्रितम्‌। आत्मरूपगुणोपेतां न कामयसि मोहिताम्‌
- **Translation**: 

---

### Verse 13 (Narsihma Puran 0.753)
- **Original**: 29 लतेब पादपे लग्ना काम त्वच्छरणं गता। बाहुभ्यां सम्परिष्वज्य निवसामि शुत्रिस्मिता
- **Translation**: 

---

### Verse 14 (Narsihma Puran 0.754)
- **Original**: 30 यम उयाच अन्यं श्रयस्व सुओ्रोणि देवं देव्यसितेक्षणे। बस्तु ते काममोहेन चेतसा विध्रम॑ गत:। तस्य देवस्थ देवी त्वं भवेधा वरवर्णिनि
- **Translation**: 

---

### Verse 15 (Narsihma Puran 0.755)
- **Original**: 31 ईप्सितां सर्वभूतानां वर्या शंसन्ति मानवा:। सुभद्रां चास्सबांड्रीं संस्कृतां परिचक्षते
- **Translation**: 

---

### Verse 16 (Narsihma Puran 0.756)
- **Original**: 32 तत्कृते5पि सुविद्वांसों न करिष्यन्ति दूषणम्‌। परिताप॑ महाप्राज़े न करिष्ये दृदक्त:
- **Translation**: 

---

### Verse 17 (Narsihma Puran 0.757)
- **Original**: 33 चित्त मे निर्मल भट्ठे विष्णौ रुद्रे च संस्थितम्‌। अत: पयाप॑ नु नेच्छामि धर्मचित्तों दृढत्॒त:
- **Translation**: 

---

### Verse 18 (Narsihma Puran 0.758)
- **Original**: 3ड श्रीनरसिंहपुराण
- **Translation**: 

---

### Verse 19 (Narsihma Puran 0.759)
- **Original**: [ अध्याय 12 यम बोले-- यहित्र! कुत्सित लोकव्यवहास्को किनदा ब्रह्माजोने भी की है। इस संसासके लोग ओह? पुरुषोंद्वारा आचरित धर्मका ही अनुसरण करते हैं। इसलिये श्रेष्ठ चुरुषकों चाहिये कि वह उत्तम धर्मका ही आचरण करे और निन्दित कर्मको यत्लपूर्वक त्याग दे--यही धर्मका लक्षण है। ब्रेप
- **Translation**: 

---

### Verse 20 (Narsihma Puran 0.760)
- **Original**: ्न पुरुष जिस-जिस कर्मका आचरण करता है, उसीको अन्य लोग भो आचरणमें लाते हैं और बह जिसे प्रमाणित कर देता है, लोग उसीका अनुसरण करते हैं। सुभगे! मैं तो तुम्हारे इस वचनकों अत्यन्त पापपूर्ण समझता हूँ। इतना हो नहीं, मैं इसे सब धर्मों और विशेषत: समस्त लोकोंके घिपरीत मानता हूँ। मुझसे अन्य जो कोई भी रूप और शोलमें विशिष्ट हो, उसके साथ तुम आनन्दपूर्वक रहो; मैं तुम्हारा पति नहों हो सकता। भद्दे! मैं दृढ़तापूर्वक उत्तम ब्रतका पालन करनतेबाला हूँ, अत: अपने शरीस्से तुम्हारे शरोरका स्पर्श वहीं करूँगा। जो बहितको ग्रहण करता है, उसे मुनियोन 'पापी' कहा है
- **Translation**: 

---

