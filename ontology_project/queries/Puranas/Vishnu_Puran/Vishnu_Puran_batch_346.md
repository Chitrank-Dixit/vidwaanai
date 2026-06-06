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

### Verse 1 (Vishnu Puran 0.6901)
- **Original**: समाधिविज्ञानावगतार्थक्षानु- अहं तस्मै चकार नात्यान्तिकमेतदद्वादशाब्द तब ओजरनन भविष्यतीति
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6902)
- **Original**: असावपि प्रति- गृह्योदकाझलिं मुनिश्ञापप्रदानायोद्यतो भगव- तयमस्मवुरुनहिस्येन॑ कुलदेवताभूतमाचार्य झप्तुपिति मदयन्त्या स्वपल्या अ्रसादितस्सस्था- म्युदरक्षणार्थ तच्छापाग्बु नोव्यां न चाकाशे चिक्षेप कि तु तेनैव स्वपदोी सिषेत्
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6903)
- **Original**: तेन च क्रोधाश्रितेनाग्बुना दग्धच्छायौ तत्पादो कल्पाषता- मुपगतौ ततस्स कल्माषपादसंज्ञामवाप
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6904)
- **Original**: वसिष्ठझ्ापाश्च षष्टे षष्ठे काले राक्षसस्वभाव- मेत्याटव्याँ पर्यटक्षनेकशो मानुषानभक्षयत्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6905)
- **Original**: एकदा तु भार्यासड्जतं दरदर्श
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6906)
- **Original**: तयोश्ल तमतिभीषण्ण राक्षस- ब्राह्मण जग्राह
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6907)
- **Original**: ततस्सा ब्राह्मणी बहुशस्तमभियाचितवती
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6908)
- **Original**: प्रसीदेक्ष्वाकु- कुलछतिलकभूतस्त्व॑ महाराजो मित्रसहो न राक्षस: उन्ते प्राप्य्सीति
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6909)
- **Original**: हाप्वा चैब साग्रि अखिलेश
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6910)
- **Original**: ततस्तस्य द्वादशाब्दपर्यये.. विमुक्तशापस्य खीविषयाभिलाधषिणो मदयन्ती त॑ स्मारयामास
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6911)
- **Original**: तदनन्तर राजाके यह कहनेपर कि 'भगवन्‌ आपहोने ऐसी आज्ञा की थी,' वसिष्ठजी यद कहते हुए कि “क्या मैंने ही ऐसा कहा था ?' फिर समाधिस्थ हो गये
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6912)
- **Original**: सम्ाधिद्वाण यथार्थ बात जानकर उन्होंने राडापर अनुग्रह करते हुए कहा, “तू अधिक दिन नरमौस भोजन न ऊरेगा, केवल बारह वर्ष हो तुझे ऐसा करना होगा”
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6913)
- **Original**: वसिष्ठजीके ऐसा कहनेपर राजा सौदास भी अपनी मकलिमें जल लेकर मुनीश्रस्को शाप देनेके ल्त्ये उच्यत हुआ । किन्तु अपनी पत्नी मदयन्तीद्वारा। भगवन्‌ ! ये हमारे कुलगुरु हैं, इग कुलटेबरूप आचार्यको शाप देना डचित नहीं है'--पेसा कहे जानेसे शान्‍्त हो गया तथा अन्न और मेघकी रक्षाके कारण ठस ज्ञाप-जलकों पृथिवी या आकाशमें नहीं फेंका, बल्कि उससे अपने पैरॉको ही भिगों लिया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6914)
- **Original**: उस क्रोधयुक्त जलसे उसके पैर झुलसकर कल्पाषवर्ण (चितकबरें) हो गये। तभीसे उनका नाम कल्माषपाद दुआ
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6915)
- **Original**: तथा वसिष्ठजोके शापके ब्रभावसे छठे कालमें अर्थात्‌ तोसरे दिनके अन्तिम भागमें बह राक्षस-स्वभाव धारणकर बनमें घूमते हुए. अनेकों मनुष्योंको खाने लगा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6916)
- **Original**: एक दिन उसने एक मुनीश्चरकों ऋतुकाऊफे समय अपनी भार्यासे सज़म करते देखा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6917)
- **Original**: उस अति भीषण गराक्षस-रूपको देखकर भयसे भागते हुए उन दम्पतियोमेंसे उसने ब्राह्मणक्रो पकड़ लिया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6918)
- **Original**: तब ब्राह्मणीने उससे नाना प्रकारसे प्रार्थना की और कहा--- हे शजन्‌ ! प्रसन्न होइये। आप राक्षस नहीं हैं अत्कि इक्ष्याकुकुलतिलक महाराज मित्रसह है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6919)
- **Original**: आप ख्री-संयोगके सुखक जाननेबाले +
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6920)
- **Original**: हैं; मैं अतृप्त हूँ, मेरे पतिको मारना आपको उचित नहीं है ।' इस प्रकार ठसके नयना प्रकारसे विल्लाप करनेपर भी उसने उस ब्राह्मणकों इस प्रकार भक्षण कर छिया जैसे बाघ अपने अभिमत पशुकों वनमें फ्कड़कर खा जाता नं
- **Translation**: 

---

